from django.db import models
from django.core import signing
from modelcluster.models import ClusterableModel, ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from django.utils import timezone


def get_intance_path(instance, file_name):
    return "documents/{}/{}".format(instance.pk, file_name)


class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        context["organizations"] = Organization.objects.filter(published=True)
        return context


class Organization(ClusterableModel):
    published = models.BooleanField(
        default=False, verbose_name="Je organizacija objavljena?"
    )
    is_complete = models.BooleanField(default=False, verbose_name="Je prijava končana?")
    signup_time_start = models.DateTimeField(
        blank=True, null=True, verbose_name="Čas začetka prijave"
    )
    signup_time = models.DateTimeField(
        blank=True, null=True, verbose_name="Čas končane prijave"
    )
    #
    name = models.CharField(
        max_length=512,
        default="",
        verbose_name="Uradno ime organizacije (iz AJPES)",
        blank=True,
    )
    additional_names = models.TextField(
        verbose_name="Druga imena, pod katerimi je organizacija poznana (kratice, okrajšave)",
        default="",
        blank=True,
    )
    contact_name = models.CharField(
        verbose_name="Kontakt: ime in priimek", default="", blank=True, max_length=128
    )
    contact_email = models.EmailField(
        verbose_name="Kontakt: e-pošta", default="", blank=True, max_length=128
    )
    contact_phone = models.CharField(
        verbose_name="Kontakt: telefon", default="", blank=True, max_length=128
    )
    web_page = models.URLField(
        max_length=512, verbose_name="Spletna stran", default="", blank=True
    )
    cover_photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Slika",
    )
    tax_number = models.CharField(
        max_length=32, verbose_name="Davčna številka", default="", blank=True
    )
    #
    mission = models.TextField(
        verbose_name="Poslanstvo organizacije (do 500 znakov)", default="", blank=True
    )
    description = models.TextField(
        verbose_name="Kratek opis organizacije (do 1500 znakov)", default="", blank=True
    )
    area = models.ManyToManyField(
        "Area",
        blank=True,
        related_name="organization",
        verbose_name="Področje delovanja (lahko izberete več možnosti)",
        default="",
    )
    custom_area = models.CharField(
        verbose_name="Področje delovanja: Drugo", default="", blank=True, max_length=128
    )
    avg_revenue = models.CharField(
        max_length=16,
        verbose_name="Povprečni letni proračun v zadnjih treh letih",
        default="",
        blank=True,
    )
    employed = models.IntegerField(
        verbose_name="Število zaposlenih v zadnjem zaključenem letu",
        default=0,
        blank=True,
    )
    is_charity = models.BooleanField(
        default=False,
        verbose_name="Organizacija ima status humanitarne organizacije",
        blank=True,
    )
    has_public_interest = models.BooleanField(
        default=False,
        verbose_name="Organizacija ima status delovanja v javnem interesu",
        blank=True,
    )
    is_voluntary = models.BooleanField(
        default=False,
        verbose_name="Organizacija je vpisana v evidenco prostovoljskih organizacij",
        blank=True,
    )
    zero5 = models.BooleanField(
        default=False,
        verbose_name="Organizacija je na seznamu upravičencev do 0,5 dohodnine",
        blank=True,
    )
    #
    has_supervisory_board = models.BooleanField(
        default=False,
        verbose_name="Organizacija ima nadzorni odbor, ki se je v preteklem letu srečal",
        blank=True,
    )
    supervisory_board_dates = models.CharField(
        verbose_name="Datumi srečanj v preteklem letu (nadzorni odbor)",
        default="",
        blank=True,
        max_length=512,
    )
    has_management_board = models.BooleanField(
        default=False,
        verbose_name="Organizacija ima upravni odbor, ki se je v preteklem letu srečal",
        blank=True,
    )
    management_board_dates = models.CharField(
        verbose_name="Datumi srečanj v preteklem letu (upravni odbor)",
        default="",
        blank=True,
        max_length=512,
    )
    has_council = models.BooleanField(
        default=False,
        verbose_name="Organizacija ima svet zavoda, ki se je v preteklem letu srečal",
        blank=True,
    )
    council_dates = models.CharField(
        verbose_name="Datumi srečanj v preteklem letu (svet zavoda)",
        default="",
        blank=True,
        max_length=512,
    )
    has_other_board = models.BooleanField(
        default=False,
        verbose_name="Organizacija ima drug organ, ki se je v preteklem letu srečal",
        blank=True,
    )
    other_board_name = models.CharField(
        verbose_name="Ime organa", default="", blank=True, max_length=128
    )
    other_board_dates = models.CharField(
        verbose_name="Datumi srečanj v preteklem letu (drug organ)",
        default="",
        blank=True,
        max_length=512,
    )
    #
    has_minutes_meeting = models.BooleanField(
        default=False, verbose_name="Ali organizacija vodi zapisnike sej?"
    )
    minutes_meeting = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Priloga: Zapisnik zadnje seje",
        blank=True,
        null=True,
    )
    #
    strategic_planning = models.BooleanField(
        default=False, verbose_name="Ali organizacija strateško načrtuje?"
    )
    has_milestiones_description = models.BooleanField(
        default=False,
        verbose_name="Ali organizacija spremlja doseganje strateških ciljev?",
    )
    milestiones_description = models.TextField(
        verbose_name="Kratek opis kako organizacija spremlja doseganje strateških ciljev (do 500 znakov)",
        default="",
        blank=True,
    )
    has_strategic_goals = models.BooleanField(
        default=False,
        verbose_name="Ali organizacija vodi pisna poročila o spremljanju stateških ciljev?",
    )
    strategic_goals = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Priloga: Pisna poročila o spremljanju stateških ciljev",
        blank=True,
        null=True,
    )
    #
    finance_report = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Priloga: Finančno poročilo",
        blank=True,
        null=True,
    )
    finance_report_ajpes = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Priloga: Finančno poročilo, ki je bilo oddano na AJPES",
        blank=True,
        null=True,
    )
    has_audited_report = models.BooleanField(
        default=False,
        verbose_name="Ali je organizacija dolžna revidirati svoja finančna poročila?",
    )
    audited_report = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Priloga: Revidirano poročilo",
        blank=True,
        null=True,
    )
    has_finance_plan = models.BooleanField(
        default=False,
        verbose_name="Ali ima organizacija finančni načrt za tekoče leto?",
    )
    finance_plan = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Priloga: Finančni načrt za tekoče leto",
        blank=True,
        null=True,
    )
    has_given_loans = models.BooleanField(
        default=False, verbose_name="Ali organizacija daje posojila povezanim osebam?"
    )
    given_loan = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Priloga: Seznam danih posojil",
        blank=True,
        null=True,
    )
    has_received_loans = models.BooleanField(
        default=False,
        verbose_name="Ali organizacija prejema posojila od povezanih oseb?",
    )
    received_loans = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Priloga: Seznam prejetih posojil",
        blank=True,
        null=True,
    )
    has_payment_classes = models.BooleanField(
        default=False,
        verbose_name="Ali ima organizacija akt o sistematizaciji delovnih mest in plačnih razredov?",
    )
    payment_classes = models.FileField(
        upload_to=get_intance_path,
        verbose_name="Priloga: Akt o sistematizaciji delovnih mest in plačnih razredov",
        blank=True,
        null=True,
    )
    wages_ratio = models.CharField(
        verbose_name="Kakšno je razmerje med najvišjo in povprečno plačo v organizaciji?",
        default="",
        blank=True,
        max_length=256,
    )
    #
    has_published_work_reports = models.BooleanField(
        default=False, verbose_name="Organizacija ima objavljena letna poročila o delu"
    )
    published_work_reports_url = models.URLField(
        max_length=512,
        verbose_name="URL do objavljenih letnih poročil o delu",
        blank=True,
        null=True,
    )
    has_published_financial_reports = models.BooleanField(
        default=False,
        verbose_name="Organizacija ima objavljena letna finančna poročila",
    )
    published_financial_reports_url = models.URLField(
        max_length=512,
        verbose_name="URL do objavljenih finančnih poročil",
        blank=True,
        null=True,
    )
    has_published_executive_salaries = models.BooleanField(
        default=False, verbose_name="Objavljene so plače vodstva"
    )
    published_executive_salaries_url = models.URLField(
        max_length=512,
        verbose_name="URL do objavljenih plač vodstva",
        blank=True,
        null=True,
    )
    has_published_salary_ratio = models.BooleanField(
        default=False, verbose_name="Objavljeno je razmerje med plačami"
    )
    published_salary_ratio_url = models.URLField(
        max_length=512,
        verbose_name="URL do objavljenih razmerij med plačami",
        blank=True,
        null=True,
    )
    has_published_employee_list = models.BooleanField(
        default=False, verbose_name="Objavljen je seznam ključnih zaposlenih"
    )
    published_employee_list_url = models.URLField(
        max_length=512,
        verbose_name="URL do objavljenega seznama ključnih zaposlenih",
        blank=True,
        null=True,
    )
    has_published_board_members = models.BooleanField(
        default=False, verbose_name="Obljavljeni so člani nadzornega/upravnega odbora"
    )
    published_board_members_url = models.URLField(
        max_length=512,
        verbose_name="URL do objavljenega seznama članov odbora",
        blank=True,
        null=True,
    )
    has_published_financial_plan = models.BooleanField(
        default=False, verbose_name="Objavljen je finančni načrt za tekoče leto"
    )
    published_financial_plan_url = models.URLField(
        max_length=512,
        verbose_name="URL do objavljenega finančnega načrta za tekoče leto",
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
    def edit_key(self):
        return signing.dumps(self.pk, salt="ORG_EDIT_KEY")

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.signup_time_start = timezone.now()

        if self.is_complete and not self.signup_time:
            self.signup_time = timezone.now()

        super().save(*args, **kwargs)

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
        InlinePanel("links", label="Družbeni mediji"),
        ImageChooserPanel("cover_photo"),
        FieldPanel("tax_number"),
        #
        FieldPanel("mission"),
        FieldPanel("description"),
        FieldPanel("area"),
        FieldPanel("custom_area"),
        FieldPanel("avg_revenue"),
        FieldPanel("employed"),
        FieldPanel("is_charity"),
        FieldPanel("has_public_interest"),
        FieldPanel("is_voluntary"),
        FieldPanel("zero5"),
        #
        FieldPanel("has_supervisory_board"),
        FieldPanel("supervisory_board_dates"),
        InlinePanel("supervisory_board_members", label="Člani nadzornega odbora"),
        FieldPanel("has_management_board"),
        FieldPanel("management_board_dates"),
        InlinePanel("management_board_members", label="Člani upravnega odbora"),
        FieldPanel("has_council"),
        FieldPanel("council_dates"),
        InlinePanel("council_members", label="Člani sveta zavoda"),
        FieldPanel("has_other_board"),
        FieldPanel("other_board_name"),
        FieldPanel("other_board_dates"),
        InlinePanel("other_board_members", label="Člani organa"),
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
            "criteria", label="Točkovnik", classname="criteria_panel", max_num=1
        ),
    ]

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Organizacija"
        verbose_name_plural = "Organizacije"


ROLE_CHOICES = [
    ("1", "Član"),
    ("2", "Predstavnik uporabnikov"),
    ("3", "Predstavnik zaposlenih"),
    ("4", "Predstavnik ustanoviteljev"),
    ("5", "Imenovan na podlagi sorodstvenih/prijateljskih vezi"),
    ("6", "Neodvisni predstavnik"),
    ("7", "Drugo:"),
]


class SupervisoryBoardMember(models.Model):
    organization = ParentalKey('Organization', on_delete=models.CASCADE, related_name="supervisory_board_members")
    name = models.CharField(max_length=512, default="", verbose_name="Ime in priimek")
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default="1", verbose_name="Povezava z organizacijo")
    custom_role = models.CharField(
        verbose_name="Povezava z organizacijo: Drugo",
        default="",
        blank=True,
        max_length=128,
    )
    is_paid = models.BooleanField(
        default=False, verbose_name="Ali za svoje delo v odboru prejema nadomestilo"
    )


class ManagementBoardMember(models.Model):
    organization = ParentalKey('Organization', on_delete=models.CASCADE, related_name="management_board_members")
    name = models.CharField(max_length=512, default="", verbose_name="Ime in priimek")
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default="1", verbose_name="Povezava z organizacijo")
    custom_role = models.CharField(
        verbose_name="Povezava z organizacijo: Drugo",
        default="",
        blank=True,
        max_length=128,
    )
    is_paid = models.BooleanField(
        default=False, verbose_name="Ali za svoje delo v odboru prejema nadomestilo"
    )


class CouncilBoardMember(models.Model):
    organization = ParentalKey('Organization', on_delete=models.CASCADE, related_name="council_members")
    name = models.CharField(max_length=512, default="", verbose_name="Ime in priimek")
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default="1", verbose_name="Povezava z organizacijo")
    custom_role = models.CharField(
        verbose_name="Povezava z organizacijo: Drugo",
        default="",
        blank=True,
        max_length=128,
    )
    is_paid = models.BooleanField(
        default=False, verbose_name="Ali za svoje delo v odboru prejema nadomestilo"
    )


class OtherBoardMember(models.Model):
    organization = ParentalKey('Organization', on_delete=models.CASCADE, related_name="other_board_members")
    name = models.CharField(max_length=512, default="", verbose_name="Ime in priimek")
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default="1", verbose_name="Povezava z organizacijo")
    custom_role = models.CharField(
        verbose_name="Povezava z organizacijo: Drugo",
        default="",
        blank=True,
        max_length=128,
    )
    is_paid = models.BooleanField(
        default=False, verbose_name="Ali za svoje delo v odboru prejema nadomestilo"
    )


class Link(models.Model):
    organization = ParentalKey(
        "Organization", on_delete=models.CASCADE, related_name="links"
    )

    url = models.URLField(verbose_name="Povezava", default="", blank=True)


class Criteria(models.Model):
    organization = ParentalKey(
        "Organization", on_delete=models.CASCADE, related_name="criteria"
    )

    control_of_business_1 = models.IntegerField(
        default=0,
        verbose_name="1.1 - Število sestankov nadzornega/upravnega odbora v zadnjem letu",
    )
    control_of_business_2 = models.IntegerField(
        default=0,
        verbose_name="1.2 - Število neodvisnih članov nadzornega/upravnega odbora, ki ima glasovalno pravico",
    )
    control_of_business_3 = models.IntegerField(
        default=0, verbose_name="1.3 - Odstotek neodvisnih članov z glasovalno pravico"
    )
    control_of_business_4 = models.IntegerField(
        default=0, verbose_name="1.4 - Organizacija ima zapisnike sej"
    )

    strategic_planning_2_1 = models.IntegerField(
        default=0, verbose_name="2.1 - Organizacija ima strateški načrt"
    )
    strategic_planning_2_2 = models.IntegerField(
        default=0,
        verbose_name="2.2 - Organizacija spremlja doseganje strateškega načrta",
    )
    strategic_planning_2_3 = models.IntegerField(
        default=0,
        verbose_name="2.3 - Organizacija pripravlja poročila o spremljanju napredka pri doseganju strateških ciljev",
    )

    financial_management_3_1 = models.IntegerField(
        default=0,
        verbose_name="3.1 - Odstotek sredstev, ki jih porabi za izvedbo programa",
    )
    financial_management_3_2 = models.IntegerField(
        default=0,
        verbose_name="3.2 - Odstotek sredstev, ki jh organizacija porabi za splošno delovanje",
    )
    financial_management_3_3 = models.IntegerField(
        default=0,
        verbose_name="3.3 - Znesek, ki ga organizacija porabi na vsakih zbranih 100 €",
    )
    financial_management_3_4_1 = models.IntegerField(
        default=0, verbose_name="3.4.1 - Viri sredstev"
    )
    financial_management_3_4_2 = models.IntegerField(
        default=0, verbose_name="3.4.2 - Delež prihodkov iz navečjega posameznega vira"
    )
    financial_management_3_5_1 = models.IntegerField(
        default=0, verbose_name="3.5.1 - Organizacija daje posojila povezanim osebam"
    )
    financial_management_3_5_2 = models.IntegerField(
        default=0,
        verbose_name="3.5.2 - Organizacija prejema posojila od povezanih oseb",
    )
    financial_management_3_6 = models.IntegerField(
        default=0,
        verbose_name="3.6 - Razmerje med najvišjo in povprečno plačo v organizaciji",
    )

    transparency_of_organizations_4_1 = models.IntegerField(
        default=0,
        verbose_name="4.1 - Organizacija ima objavljena letna poročila o delu",
    )
    transparency_of_organizations_4_2 = models.IntegerField(
        default=0, verbose_name="4.2 - Letna poročila o delu so razumljiva"
    )
    transparency_of_organizations_4_2_1 = models.IntegerField(
        default=0,
        verbose_name="4.2.1 - Organizacija ima objavljena letna finančna poročila",
    )
    transparency_of_organizations_4_2_2 = models.IntegerField(
        default=0, verbose_name="4.2.2 - Finančna poročila so razumljiva"
    )
    transparency_of_organizations_4_2_3 = models.IntegerField(
        default=0,
        verbose_name="4.2.3 - Finančna poročila so razdeljena po programih in vrstah stroškov in prihodkov",
    )
    transparency_of_organizations_4_3 = models.IntegerField(
        default=0, verbose_name="4.3 - Objavljene so plače vodstva"
    )
    transparency_of_organizations_4_4 = models.IntegerField(
        default=0, verbose_name="4.4 - Objavljeno je razmerje med plačami"
    )
    transparency_of_organizations_4_5 = models.IntegerField(
        default=0, verbose_name="4.5 - Objavljen je seznam ključnih zaposlenih"
    )
    transparency_of_organizations_4_6 = models.IntegerField(
        default=0, verbose_name="4.6 - Obljavljeni so člani nadzornega/upravnega odbora"
    )
    transparency_of_organizations_4_7 = models.IntegerField(
        default=0, verbose_name="4.7 - Objavljen je finančni načrt za tekoče leto"
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

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("control_of_business_1"),
                FieldPanel("control_of_business_2"),
                FieldPanel("control_of_business_3"),
                FieldPanel("control_of_business_4"),
            ],
            heading="Kriterij 1: Nadzor nad poslovanjem",
        ),
        MultiFieldPanel(
            [
                FieldPanel("strategic_planning_2_1"),
                FieldPanel("strategic_planning_2_2"),
                FieldPanel("strategic_planning_2_3"),
            ],
            heading="Kriterij 2: Strateško načrtovanje",
        ),
        MultiFieldPanel(
            [
                FieldPanel("financial_management_3_1"),
                FieldPanel("financial_management_3_2"),
                FieldPanel("financial_management_3_3"),
                FieldPanel("financial_management_3_4_1"),
                FieldPanel("financial_management_3_4_2"),
                FieldPanel("financial_management_3_5_1"),
                FieldPanel("financial_management_3_5_2"),
                FieldPanel("financial_management_3_6"),
            ],
            heading="Kriterij 3: Finančno upravljanje",
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
            heading="Kriterij 4: Transparentnost organizacij",
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
