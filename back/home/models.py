from django import forms
from django.db import models
from django.core import signing
from django.conf import settings
from django.utils import timezone
from modelcluster.models import ClusterableModel, ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

import requests


def try_send_mail_updated_org(id, inst):
    try:
        to_mail = "dobrodelen@cnvos.si"
        subject = '[dobrodelen.si] Organizacija "{name}" je posodobila podatke'.format(
            name=inst.name
        )
        content = """
            Hej, to je avtomatsko sporočilo da je nekdo spremenil podatke organizaciji!

            Ime organizacije: {name}
            Povezava do profila: http://dobrotest.djnd.si/organizacija/{id}
            Povezava do admin strani: http://dobrotest.djnd.si/admin/home/organization/edit/{id}/

            LP
        """.format(
            id=id, name=inst.name
        )

        if settings.MAILGUN_API and settings.MAILGUN_ACCESS_KEY:
            requests.post(
                settings.MAILGUN_API,
                auth=("api", settings.MAILGUN_ACCESS_KEY),
                data={
                    "from": settings.FROM_MAIL,
                    "to": to_mail,
                    "subject": subject,
                    "text": content,
                },
            )
            print("Sent mail - organization updated:", id)

    except Exception as e:
        print("Failed to send mail - organization updated:", id)
        print(e)


def get_intance_path(instance, file_name):
    return "documents/{}/{}".format(instance.pk, file_name)


class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        context["organizations"] = Organization.objects.filter(published=True)
        return context


class Organization(ClusterableModel):
    published = models.BooleanField(
        default=False, verbose_name="Published?"
    )
    is_complete = models.BooleanField(default=False, verbose_name="Signup complete?")
    signup_time_start = models.DateTimeField(
        blank=True, null=True, verbose_name="Signup started time"
    )
    signup_time = models.DateTimeField(
        blank=True, null=True, verbose_name="Signup finished time"
    )
    #
    name = models.CharField(
        max_length=512,
        default="",
        verbose_name="Legal organization name",
        blank=True,
    )
    additional_names = models.TextField(
        verbose_name="Other organization names (short names, acronyms, etc.)",
        default="",
        blank=True,
    )
    contact_name = models.CharField(
        verbose_name="Contact person: name", default="", blank=True, max_length=128
    )
    contact_email = models.EmailField(
        verbose_name="Contact person: email", default="", blank=True, max_length=128
    )
    contact_phone = models.CharField(
        verbose_name="Contact person: phone", default="", blank=True, max_length=128
    )
    web_page = models.URLField(
        max_length=512, verbose_name="Website", default="", blank=True
    )
    cover_photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Image",
    )
    tax_number = models.CharField(
        max_length=32, verbose_name="Tax number", default="", blank=True
    )
    #
    mission = models.TextField(
        verbose_name="Organization mission statement (max. 500 characters)", default="", blank=True
    )
    description = models.TextField(
        verbose_name="Short description of organization (max. 1500 characters)", default="", blank=True
    )
    area = models.ManyToManyField(
        "Area",
        blank=True,
        related_name="organization",
        verbose_name="Area of operation (can select multiple)",
        default="",
    )
    custom_area = models.CharField(
        verbose_name="Area of operation: Other", default="", blank=True, max_length=128
    )
    region = models.ManyToManyField(
        "Region",
        blank=True,
        related_name="organization",
        verbose_name="Region (can select multiple)",
        default="",
    )
    avg_revenue = models.IntegerField(
        verbose_name="Average annual budget for the last three years",
        default=0,
        blank=True,
    )
    employed = models.IntegerField(
        verbose_name="Number of employees in the last completed year",
        default=0,
        blank=True,
    )
    is_charity = models.BooleanField(
        default=False,
        verbose_name="Organization has the status of a humanitarian organization",
        blank=True,
    )
    has_public_interest = models.BooleanField(
        default=False,
        verbose_name="Organization has the status of acting in the public interest",
        blank=True,
    )
    is_voluntary = models.BooleanField(
        default=False,
        verbose_name="Organization is entered in the register of voluntary organizations",
        blank=True,
    )
    # FIXME: Macedonia?
    zero5 = models.BooleanField(
        default=False,
        verbose_name="Organizacija je na seznamu upravičencev do 0,5 dohodnine",
        blank=True,
    )
    #
    has_supervisory_board = models.BooleanField(
        default=False,
        verbose_name="The organization has a supervisory board that met last year",
        blank=True,
    )
    supervisory_board_dates = models.CharField(
        verbose_name="Dates of meetings in the previous year (supervisory board)",
        default="",
        blank=True,
        max_length=512,
    )
    has_management_board = models.BooleanField(
        default=False,
        verbose_name="The organization has a management board that met last year",
        blank=True,
    )
    management_board_dates = models.CharField(
        verbose_name="Dates of meetings in the previous year (management board)",
        default="",
        blank=True,
        max_length=512,
    )
    has_council = models.BooleanField(
        default=False,
        verbose_name="Organization has a council that met last year",
        blank=True,
    )
    council_dates = models.CharField(
        verbose_name="Dates of meetings in the previous year (council)",
        default="",
        blank=True,
        max_length=512,
    )
    has_other_board = models.BooleanField(
        default=False,
        verbose_name="The organization has another body that has met in the past year",
        blank=True,
    )
    other_board_name = models.CharField(
        verbose_name="Name of other body", default="", blank=True, max_length=128
    )
    other_board_dates = models.CharField(
        verbose_name="Dates of meetings in the previous year (other body)",
        default="",
        blank=True,
        max_length=512,
    )
    #
    has_minutes_meeting = models.BooleanField(
        default=False, verbose_name="Does the organization keep minutes of meetings?"
    )
    minutes_meeting = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Attachment: Minutes of last meetings",
        blank=True,
        null=True,
    )
    #
    strategic_planning = models.BooleanField(
        default=False, verbose_name="Does the organization do strategic planning?"
    )
    has_milestiones_description = models.BooleanField(
        default=False,
        verbose_name="Does the organization monitor the achievement of strategic objectives?",
    )
    milestiones_description = models.TextField(
        verbose_name="Brief description of how the organization monitors the achievement of strategic objectives (max. 500 characters)",
        default="",
        blank=True,
    )
    has_strategic_goals = models.BooleanField(
        default=False,
        verbose_name="Does the organization keep written reports on the monitoring of strategic objectives?",
    )
    strategic_goals = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Attachment: Written reports on the monitoring of strategic objectives",
        blank=True,
        null=True,
    )
    #
    finance_report = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Attachment: Financial report",
        blank=True,
        null=True,
    )
    finance_report_ajpes = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Attachment: Financial report, submitted to public legal record agency",
        blank=True,
        null=True,
    )
    has_audited_report = models.BooleanField(
        default=False,
        verbose_name="Does the organization have audited financial reports?",
    )
    audited_report = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Attachment: Audited financial report",
        blank=True,
        null=True,
    )
    has_finance_plan = models.BooleanField(
        default=False,
        verbose_name="Does the organization have a financial plan for the current year?",
    )
    finance_plan = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Attachment: Financial plan for the current year",
        blank=True,
        null=True,
    )
    has_given_loans = models.BooleanField(
        default=False, verbose_name="Does the organization provide loans to related parties?"
    )
    given_loan = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Attachment: List of provided loans",
        blank=True,
        null=True,
    )
    has_received_loans = models.BooleanField(
        default=False,
        verbose_name="Does the organization receive loans from related parties?",
    )
    received_loans = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Attachment: List of received loans",
        blank=True,
        null=True,
    )
    has_payment_classes = models.BooleanField(
        default=False,
        verbose_name="Does the organization have an act on the systematization of jobs and pay grades?",
    )
    payment_classes = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Attachment: Act on the systematization of jobs and pay grades",
        blank=True,
        null=True,
    )
    wages_ratio = models.CharField(
        verbose_name="What is the ratio between the highest and average wage in an organization?",
        default="",
        blank=True,
        max_length=256,
    )
    #
    has_published_work_reports = models.BooleanField(
        default=False, verbose_name="Organization has published annual activity reports"
    )
    published_work_reports_url = models.URLField(
        max_length=512,
        verbose_name="URL to published annual activity reports",
        blank=True,
        null=True,
    )
    has_published_financial_reports = models.BooleanField(
        default=False,
        verbose_name="Organization has published annual financial reports",
    )
    published_financial_reports_url = models.URLField(
        max_length=512,
        verbose_name="URL to published annual financial reports",
        blank=True,
        null=True,
    )
    has_published_executive_salaries = models.BooleanField(
        default=False, verbose_name="Organization has published management remuneration"
    )
    published_executive_salaries_url = models.URLField(
        max_length=512,
        verbose_name="URL to published management remuneration",
        blank=True,
        null=True,
    )
    has_published_salary_ratio = models.BooleanField(
        default=False, verbose_name="Organization has published wage ratios"
    )
    published_salary_ratio_url = models.URLField(
        max_length=512,
        verbose_name="URL to published wage ratios",
        blank=True,
        null=True,
    )
    has_published_employee_list = models.BooleanField(
        default=False, verbose_name="Organization has published a list of key employees"
    )
    published_employee_list_url = models.URLField(
        max_length=512,
        verbose_name="URL to the published list of key employees",
        blank=True,
        null=True,
    )
    has_published_board_members = models.BooleanField(
        default=False, verbose_name="Organization has published a list of board members"
    )
    published_board_members_url = models.URLField(
        max_length=512,
        verbose_name="URL to the published list of board members",
        blank=True,
        null=True,
    )
    has_published_financial_plan = models.BooleanField(
        default=False, verbose_name="Organization has published the financial plan for the current year"
    )
    published_financial_plan_url = models.URLField(
        max_length=512,
        verbose_name="URL to the published financial plan for the current year",
        blank=True,
        null=True,
    )
    #

    @property
    def stars(self):
        if self.criteria and self.criteria.count() > 0:
            return self.criteria.first().stars
        return -1

    @property
    def points(self):
        criteria = self.criteria.first()
        fields = [
            f.name
            for f in criteria.__class__._meta.fields
            if f.name not in ["id", "organization", "stars"]
        ]

        def field_to_object(f):
            verbose_name = criteria.__class__._meta.get_field(f).verbose_name
            return {
                "name": f,
                "verbose_name": verbose_name,
                "value": getattr(criteria, f, 0),
                "max_value": criteria.__class__.max_values.get(
                    verbose_name.split(" - ")[0], 0
                ),
            }

        values = list(map(field_to_object, fields))
        return values

    @property
    def edit_key(self):
        return signing.dumps(self.pk, salt="ORG_EDIT_KEY")

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        if is_new:
            self.signup_time_start = timezone.now()

        is_complete_first_time = self.is_complete and not self.signup_time
        if is_complete_first_time:
            self.signup_time = timezone.now()

        super().save(*args, **kwargs)

        if is_complete_first_time or self.is_complete:
            try_send_mail_updated_org(self.pk, self)

    panels = [
        FieldPanel("published"),
        FieldPanel("is_complete"),
        FieldPanel("signup_time_start"),
        FieldPanel("signup_time"),
        #
        FieldPanel("name"),
        FieldPanel("additional_names"),
        FieldPanel("contact_name"),
        FieldPanel("contact_email"),
        FieldPanel("contact_phone"),
        FieldPanel("web_page"),
        InlinePanel("links", label="Social media"),
        ImageChooserPanel("cover_photo"),
        FieldPanel("tax_number"),
        #
        FieldPanel("mission"),
        FieldPanel("description"),
        FieldPanel("area", widget=forms.CheckboxSelectMultiple),
        FieldPanel("custom_area"),
        FieldPanel("region", widget=forms.CheckboxSelectMultiple),
        FieldPanel("avg_revenue"),
        FieldPanel("employed"),
        FieldPanel("is_charity"),
        FieldPanel("has_public_interest"),
        FieldPanel("is_voluntary"),
        FieldPanel("zero5"),
        #
        FieldPanel("has_supervisory_board"),
        FieldPanel("supervisory_board_dates"),
        InlinePanel("supervisory_board_members", label="Supervisory board members"),
        FieldPanel("has_management_board"),
        FieldPanel("management_board_dates"),
        InlinePanel("management_board_members", label="Management board members"),
        FieldPanel("has_council"),
        FieldPanel("council_dates"),
        InlinePanel("council_members", label="Council members"),
        FieldPanel("has_other_board"),
        FieldPanel("other_board_name"),
        FieldPanel("other_board_dates"),
        InlinePanel("other_board_members", label="Other body members"),
        FieldPanel("has_minutes_meeting"),
        FieldPanel("minutes_meeting"),
        #
        FieldPanel("strategic_planning"),
        FieldPanel("has_milestiones_description"),
        FieldPanel("milestiones_description"),
        FieldPanel("has_strategic_goals"),
        FieldPanel("strategic_goals"),
        #
        FieldPanel("finance_report"),
        FieldPanel("finance_report_ajpes"),
        FieldPanel("has_audited_report"),
        FieldPanel("audited_report"),
        FieldPanel("has_finance_plan"),
        FieldPanel("finance_plan"),
        FieldPanel("has_given_loans"),
        FieldPanel("given_loan"),
        FieldPanel("has_received_loans"),
        FieldPanel("received_loans"),
        FieldPanel("has_payment_classes"),
        FieldPanel("payment_classes"),
        FieldPanel("wages_ratio"),
        #
        FieldPanel("has_published_work_reports"),
        FieldPanel("published_work_reports_url"),
        FieldPanel("has_published_financial_reports"),
        FieldPanel("published_financial_reports_url"),
        FieldPanel("has_published_executive_salaries"),
        FieldPanel("published_executive_salaries_url"),
        FieldPanel("has_published_salary_ratio"),
        FieldPanel("published_salary_ratio_url"),
        FieldPanel("has_published_employee_list"),
        FieldPanel("published_employee_list_url"),
        FieldPanel("has_published_board_members"),
        FieldPanel("published_board_members_url"),
        FieldPanel("has_published_financial_plan"),
        FieldPanel("published_financial_plan_url"),
        #
        #
        InlinePanel(
            "criteria", label="Критериуми", classname="criteria_panel", max_num=1
        ),
    ]

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"


ROLE_CHOICES = [
    ("1", "Член"),
    ("2", "Претставник на корисниците"),
    ("3", "Претставник на вработените"),
    ("4", "Претставник на основачите"),
    ("5", "Именуван врз основа на роднински/пријателски врски"),
    ("6", "Независен претставник"),
    ("7", "Друго:"),
]


class SupervisoryBoardMember(models.Model):
    organization = ParentalKey(
        "Organization",
        on_delete=models.CASCADE,
        related_name="supervisory_board_members",
    )
    name = models.CharField(max_length=512, default="", verbose_name="Full name")
    role = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        default="1",
        verbose_name="Role in organization",
    )
    custom_role = models.CharField(
        verbose_name="Role in organization: Other",
        default="",
        blank=True,
        max_length=128,
    )
    is_paid = models.BooleanField(
        default=False, verbose_name="Receives compensation for his work on the board"
    )


class ManagementBoardMember(models.Model):
    organization = ParentalKey(
        "Organization",
        on_delete=models.CASCADE,
        related_name="management_board_members",
    )
    name = models.CharField(max_length=512, default="", verbose_name="Full name")
    role = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        default="1",
        verbose_name="Role in organization",
    )
    custom_role = models.CharField(
        verbose_name="Role in organization: Other",
        default="",
        blank=True,
        max_length=128,
    )
    is_paid = models.BooleanField(
        default=False, verbose_name="Receives compensation for his work on the board"
    )


class CouncilBoardMember(models.Model):
    organization = ParentalKey(
        "Organization", on_delete=models.CASCADE, related_name="council_members"
    )
    name = models.CharField(max_length=512, default="", verbose_name="Full name")
    role = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        default="1",
        verbose_name="Role in organization",
    )
    custom_role = models.CharField(
        verbose_name="Role in organization: Other",
        default="",
        blank=True,
        max_length=128,
    )
    is_paid = models.BooleanField(
        default=False, verbose_name="Receives compensation for his work on the board"
    )


class OtherBoardMember(models.Model):
    organization = ParentalKey(
        "Organization", on_delete=models.CASCADE, related_name="other_board_members"
    )
    name = models.CharField(max_length=512, default="", verbose_name="Full name")
    role = models.CharField(
        max_length=2,
        choices=ROLE_CHOICES,
        default="1",
        verbose_name="Role in organization",
    )
    custom_role = models.CharField(
        verbose_name="Role in organization: Other",
        default="",
        blank=True,
        max_length=128,
    )
    is_paid = models.BooleanField(
        default=False, verbose_name="Receives compensation for his work on the board"
    )


class Link(models.Model):
    organization = ParentalKey(
        "Organization", on_delete=models.CASCADE, related_name="links"
    )

    url = models.URLField(verbose_name="Link", default="", blank=True)


class Criteria(models.Model):
    organization = ParentalKey(
        "Organization", on_delete=models.CASCADE, related_name="criteria"
    )

    control_of_business_1 = models.IntegerField(
        default=0,
        verbose_name="1.1 - Број на состаноци на не-извршниот орган",
        help_text="Број на состаноци | 5+ = 𝟓 | 4 = 𝟒 | 3 = 𝟑 | 2 = 𝟐 | 1 = 𝟏 | 0 = 𝟎 |",
    )
    control_of_business_2 = models.IntegerField(
        default=0,
        verbose_name="1.2 - Број на независни членови со право на глас во не-извршниот орган",
        help_text="Број на членови | 5+ = 𝟑 | 3-5 = 𝟐 | 1-2 = 𝟏 | 0 = 𝟎 |",
    )
    control_of_business_3 = models.IntegerField(
        default=0,
        verbose_name="1.3 - Процент на независни членови со право на глас",
        help_text="Процент на независни членови | 75+ = 𝟑 | 50-75 = 𝟐 | <50 = 𝟏 | 0 = 𝟎 |",
    )
    control_of_business_4 = models.IntegerField(
        default=0,
        verbose_name="1.4 - Организацијата води записници од одржаните состаноци",
        help_text="| Да = 𝟐 | не = 𝟎 |",
    )
    # MACEDONIA ADDED
    control_of_business_5 = models.IntegerField(
        default=0,
        verbose_name="1.5 - Организацијата има родова еднаквост во управниот орган",
        help_text="| Да = 𝟐 | не = 𝟎 |",
    )
    # MACEDONIA ADDED END

    strategic_planning_2_1 = models.IntegerField(
        default=0,
        verbose_name="2.1 - Организацијата има стратешки (или годишен) план",
        help_text="| Да = 𝟑 | не = 𝟎 |",
    )
    strategic_planning_2_2 = models.IntegerField(
        default=0,
        verbose_name="2.2 - Организацијата го мониторира (има рамка за мониторирање и презентира внатрешно прогрес) исполнувањето на стратешкиот план",
        help_text="| Да = 𝟑 | не = 𝟎 |",
    )
    strategic_planning_2_3 = models.IntegerField(
        default=0,
        verbose_name="2.3 - Организацијата подготвува извештаи од мониторирање на исполнувањето стратешките цели",
        help_text="| Да = 𝟐 | не = 𝟎 |",
    )
    # MACEDONIA ADDED
    strategic_planning_2_4 = models.IntegerField(
        default=0,
        verbose_name="2.4 - Организацијата подготвува годишен план",
        help_text="| Да = 𝟐 | не = 𝟎 |",
    )
    # MACEDONIA ADDED END

    financial_management_3_1 = models.IntegerField(
        default=0,
        verbose_name="3.1 - Процент од средствата употребени за спроведување на директни проектни активности",
        help_text="Процент на средства | 90+ = 𝟓 | 90-86 = 𝟒 | 85-76 = 𝟑 | 75-70 = 𝟐 | <70 = 𝟏 |",
    )
    financial_management_3_2 = models.IntegerField(
        default=0,
        verbose_name="3.2 - Процент на средства за тековно/оперативно работење",
        help_text="Процент од средствата | <10 = 𝟓 | 10-14 = 𝟒 | 15-24 = 𝟑 | 25-30 = 𝟐 | 30+ = 𝟏 |",
    )
    # FIXME: MACEDONIA MISSING
    financial_management_3_3 = models.IntegerField(
        default=0,
        verbose_name="3.3 - Znesek, ki ga organizacija porabi na vsakih zbranih 100 €",
        help_text="Znesek | 0-5 = 𝟓 | 6-15 = 𝟒 | 16-24 = 𝟑 | 25-30 = 𝟐 | 30+ = 𝟏 |",
    )
    # FIXME: MACEDONIA MISSING END
    financial_management_3_4_1 = models.IntegerField(
        default=0,
        verbose_name="3.4.1 - Извори на финансирање",
        help_text="Број на извори | 10+ = 𝟓 | 8-9 = 𝟒 | 6-7 = 𝟑 | 3-5 = 𝟐 | <3 = 𝟏 |",
    )
    financial_management_3_4_2 = models.IntegerField(
        default=0,
        verbose_name="3.4.2 - Удел на приходите од најголемиот извор",
        help_text="Процент од приходи | <=20 = 𝟓 | 21-30 = 𝟒 | 31-40 = 𝟑 | 41-50 = 𝟐 | 50+ = 𝟏 |",
    )
    # MACEDONIA REMOVED
    # financial_management_3_5_1 = models.IntegerField(
    #     default=0,
    #     verbose_name="3.5.1 - Organizacija daje posojila povezanim osebam",
    #     help_text="Organizacija daje posojila povezanim osebam | Да = 𝟎 | не = 𝟒 |",
    # )
    # financial_management_3_5_2 = models.IntegerField(
    #     default=0,
    #     verbose_name="3.5.2 - Organizacija prejema posojila od povezanih oseb",
    #     help_text="Organizacija prejema posojila od povezanih oseb | Да = 𝟎 | не = 𝟐 |",
    # )
    # MACEDONIA REMOVED END
    financial_management_3_6 = models.IntegerField(
        default=0,
        verbose_name="3.6 - Соодносот помеѓу највисоката и просечната плата во организацијата",
        help_text="Сооднос | <1:2 = 𝟓 | 1:2,9-1:2 = 𝟒 | 1:3,9-1:3 = 𝟑 | 1:4-1:5 = 𝟐 | >1:5 = 𝟏 |",
    )

    transparency_of_organizations_4_1 = models.IntegerField(
        default=0,
        verbose_name="4.1.1 - Организацијата има објавени наративни годишни извештаи",
        help_text="| Да = 𝟐 | не = 𝟎 |",
    )
    transparency_of_organizations_4_2 = models.IntegerField(
        default=0,
        verbose_name="4.1.2 - Наративните годишни извештаи се разбирливи",
        help_text="| Да = 𝟐 | не = 𝟎 |",
    )
    transparency_of_organizations_4_2_1 = models.IntegerField(
        default=0,
        verbose_name="4.2.1 - Организацијата има објавени годишни финансиски извештаи",
        help_text="| Да = 𝟐 | не = 𝟎 |",
    )
    transparency_of_organizations_4_2_2 = models.IntegerField(
        default=0,
        verbose_name="4.2.2 - Финансиските документи се разбирливи",
        help_text="| Да = 𝟐 | не = 𝟎 |",
    )
    transparency_of_organizations_4_2_3 = models.IntegerField(
        default=0,
        verbose_name="4.2.3 - Финансиските документи се поделени по програми и видови на трошоци и приходи",
        help_text="| Да = 𝟐 | не = 𝟎 |",
    )
    transparency_of_organizations_4_3 = models.IntegerField(
        default=0,
        verbose_name="4.3 - Објавен е надоместокот кој го добива раководството",
        help_text="| Да = 𝟏 | не = 𝟎 |",
    )
    transparency_of_organizations_4_4 = models.IntegerField(
        default=0,
        verbose_name="4.4 - Објавен е соодносот на платите",
        help_text="| Да = 𝟏 | не = 𝟎 |",
    )
    transparency_of_organizations_4_5 = models.IntegerField(
        default=0,
        verbose_name="4.5 - Објавена е листа со клучните вработени лица",
        help_text="| Да = 𝟏 | не = 𝟎 |",
    )
    transparency_of_organizations_4_6 = models.IntegerField(
        default=0,
        verbose_name="4.6 - Објавени се членовите на не-извршните органи",
        help_text="| Да = 𝟏 | не = 𝟎 |",
    )
    transparency_of_organizations_4_7 = models.IntegerField(
        default=0,
        verbose_name="4.7 - Објавен е финансискиот план за тековната година",
        help_text="| Да = 𝟏 | не = 𝟎 |",
    )

    stars = models.IntegerField(default=-1, editable=False)

    def compute_stars(self):
        fields = [
            f.name
            for f in self.__class__._meta.fields
            if f.name not in ["id", "organization"]
        ]
        points = sum(list(map(lambda f: getattr(self, f, 0), fields)))
        if points < 30:
            return 0
        if points < 35:
            return 1
        if points < 41:
            return 2
        if points < 51:
            return 3
        if points < 61:
            return 4
        return 5

    def save(self, *args, **kwargs):
        self.stars = self.compute_stars()
        super().save(*args, **kwargs)

    max_values = {
        "1.1": 5,
        "1.2": 3,
        "1.3": 3,
        "1.4": 2,
        "1.5": 2,
        "2.1": 3,
        "2.2": 3,
        "2.3": 2,
        "2.4": 2,
        "3.1": 5,
        "3.2": 5,
        "3.3": 5,
        "3.4.1": 5,
        "3.4.2": 5,
        # "3.5.1": 4,
        # "3.5.2": 2,
        "3.6": 5,
        "4.1.1": 2,
        "4.1.2": 2,
        "4.2.1": 2,
        "4.2.2": 2,
        "4.2.3": 2,
        "4.3": 1,
        "4.4": 1,
        "4.5": 1,
        "4.6": 1,
        "4.7": 1,
    }

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("control_of_business_1"),
                FieldPanel("control_of_business_2"),
                FieldPanel("control_of_business_3"),
                FieldPanel("control_of_business_4"),
                FieldPanel("control_of_business_5"),
            ],
            heading="Критериум 1. Контрола врз работата на организацијата",
        ),
        MultiFieldPanel(
            [
                FieldPanel("strategic_planning_2_1"),
                FieldPanel("strategic_planning_2_2"),
                FieldPanel("strategic_planning_2_3"),
                FieldPanel("strategic_planning_2_4"),
            ],
            heading="Критериум 2: Стратешко планирање на организациите",
        ),
        MultiFieldPanel(
            [
                FieldPanel("financial_management_3_1"),
                FieldPanel("financial_management_3_2"),
                FieldPanel("financial_management_3_3"),
                FieldPanel("financial_management_3_4_1"),
                FieldPanel("financial_management_3_4_2"),
                # FieldPanel("financial_management_3_5_1"),
                # FieldPanel("financial_management_3_5_2"),
                FieldPanel("financial_management_3_6"),
            ],
            heading="Критериум 3: финансиски менаџмент",
        ),
        MultiFieldPanel(
            [
                FieldPanel("transparency_of_organizations_4_1"),
                FieldPanel("transparency_of_organizations_4_2"),
                FieldPanel("transparency_of_organizations_4_2_1"),
                FieldPanel("transparency_of_organizations_4_2_2"),
                FieldPanel("transparency_of_organizations_4_2_3"),
                FieldPanel("transparency_of_organizations_4_3"),
                FieldPanel("transparency_of_organizations_4_4"),
                FieldPanel("transparency_of_organizations_4_5"),
                FieldPanel("transparency_of_organizations_4_6"),
                FieldPanel("transparency_of_organizations_4_7"),
            ],
            heading="Критериум 4: транспарентност на организацијата",
        ),
    ]

    def __str__(self):
        if self.organization:
            return str("Criteria for {}".format(self.organization.name))
        return str("Unknown Criteria")


class Area(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
