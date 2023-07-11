import requests
from django.conf import settings
from django.core import signing
from django.db import models
from django.forms import CheckboxInput, CheckboxSelectMultiple, MultiWidget, URLInput
from django.utils import timezone
from modelcluster.models import ClusterableModel, ParentalKey
from wagtail.admin.panels import FieldPanel, HelpPanel, InlinePanel, MultiFieldPanel
from wagtail.core.models import Page


def try_send_mail_updated_org(id, inst):
    try:
        to_mail = "lena.pensek@cnvos.si"
        subject = '[dobrodelen.si] Organizacija "{name}" je posodobila podatke'.format(
            name=inst.name
        )
        content = """
            Hej, to je avtomatsko sporočilo da je nekdo spremenil podatke organizaciji!

            Ime organizacije: {name}
            Povezava do profila: https://dobrodelen.si/organizacija/{id}
            Povezava do admin strani: https://dobrodelen.si/admin/home/organization/edit/{id}/

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


TUPLE_FIELD_SIZE = 2


class TupleField(models.Field):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = TUPLE_FIELD_SIZE
        kwargs["default"] = "0" * TUPLE_FIELD_SIZE
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        del kwargs["default"]
        return name, path, args, kwargs

    def get_internal_type(self):
        return "CharField"

    def get_prep_value(self, value):
        one, two = self.to_python(value)
        return f"{int(one)}{int(two)}"

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def to_python(self, value):
        if value is None:
            return (False, False)
        if isinstance(value, (tuple, list)):
            value = tuple(map(bool, value[:TUPLE_FIELD_SIZE]))
        else:
            if value.startswith("[") or value.startswith("("):
                strings = tuple(map(str.strip, value[1:-1].split(",")))[
                    :TUPLE_FIELD_SIZE
                ]
                value = tuple(map(lambda s: s in ("t", "True", "1"), strings))
            else:
                string_value = str(value)[:TUPLE_FIELD_SIZE]
                value = tuple(map(bool, map(int, iter(string_value))))
        size = len(value)
        if size < TUPLE_FIELD_SIZE:
            return value + (False,) * (TUPLE_FIELD_SIZE - size)
        return value

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)


class LabeledTupleCheckboxes(MultiWidget):
    template_name = "home/admin/widgets/labeled_tuple_checkboxes.html"

    def __init__(self, attrs=None):
        widgets = [
            CheckboxInput({"label": "Odgovor organizacije"}),
            CheckboxInput({"label": "CNVOS"}),
        ]
        super().__init__(widgets, attrs)


class URLInputWithLink(URLInput):
    template_name = "home/admin/widgets/url_with_link.html"


class HomePage(Page):
    pass


class Organization(ClusterableModel):
    # META INFO
    is_complete = models.BooleanField(
        default=False,
        verbose_name="Je prijava končana?",
    )
    signup_time_start = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Čas začetka prijave",
    )
    signup_time = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Čas končane prijave",
    )

    # REVIEW INFO
    review_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Datum pregleda",
    )
    review_notes = models.TextField(
        default="",
        blank=True,
        verbose_name="Opombe ocenjevalca (ni javno)",
    )
    published = models.BooleanField(
        default=False,
        verbose_name="Je organizacija objavljena?",
    )

    # OSEBNA IZKAZNICA ORGANIZACIJE
    name = models.CharField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Uradno ime organizacije (iz AJPES)",
    )
    additional_names = models.TextField(
        default="",
        blank=True,
        verbose_name="Druga imena, pod katerimi je organizacija poznana (kratice, okrajšave)",
    )
    cover_photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Slika",
    )
    address = models.CharField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Naslov organizacije",
    )
    contact_name = models.CharField(
        max_length=128,
        default="",
        blank=True,
        verbose_name="Kontakt: ime in priimek",
    )
    contact_email = models.EmailField(
        max_length=128,
        default="",
        blank=True,
        verbose_name="Kontakt: e-pošta",
    )
    contact_phone = models.CharField(
        max_length=128,
        default="",
        blank=True,
        verbose_name="Kontakt: telefon",
    )
    tax_number = models.CharField(
        max_length=32,
        default="",
        blank=True,
        verbose_name="Davčna številka",
    )
    account_number = models.CharField(
        max_length=64,
        default="",
        blank=True,
        verbose_name="Številka tekočega računa",
    )
    donation_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Povezava na spletno stran organizacije, kjer je možno donirati sredstva (če obstaja)",
    )
    web_page = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Spletna stran",
    )
    # links = related model
    region = models.ManyToManyField(
        "Region",
        default="",
        blank=True,
        related_name="organization",
        verbose_name="Regije (lahko izberete več možnosti)",
    )
    area = models.ManyToManyField(
        "Area",
        default="",
        blank=True,
        related_name="organization",
        verbose_name="Področje delovanja (lahko izberete več možnosti)",
    )
    custom_area = models.CharField(
        max_length=128,
        default="",
        blank=True,
        verbose_name="Področje delovanja: Drugo",
    )

    # avg_revenue = models.IntegerField(
    #     default=0,
    #     blank=True,
    #     verbose_name="Povprečni letni proračun v zadnjih treh letih",
    # )
    # employed = models.IntegerField(
    #     default=0,
    #     blank=True,
    #     verbose_name="Število zaposlenih v zadnjem zaključenem letu",
    # )

    # is_charity = models.BooleanField(
    #     default=False,
    #     blank=True,
    #     verbose_name="Organizacija ima status humanitarne organizacije",
    # )
    # has_public_interest = models.BooleanField(
    #     default=False,
    #     blank=True,
    #     verbose_name="Organizacija ima status delovanja v javnem interesu",
    # )
    # is_voluntary = models.BooleanField(
    #     default=False,
    #     blank=True,
    #     verbose_name="Organizacija je vpisana v evidenco prostovoljskih organizacij",
    # )
    # zero5 = models.BooleanField(
    #     default=False,
    #     blank=True,
    #     verbose_name="Organizacija je na seznamu upravičencev do 1 % dohodnine",
    # )
    # zero5_amount = models.IntegerField(
    #     default=0,
    #     blank=True,
    #     verbose_name="Višina zbranih sredstev prek 1 % dohodnine",
    # )

    # DOSTOPNOST OSNOVNIH INFORMACIJ
    has_published_key_documents = models.BooleanField(
        default=False,
        verbose_name="Kriterij 1: Organizacija ima objavljene ključne dokumente (akt o ustanovitvi in/ali statut)",
    )
    key_documents_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 1: URL do objavljenega dokumenta/podatkov",
    )
    has_published_mission = models.BooleanField(
        default=False, verbose_name="Kriterij 2: Organizacija ima objavljeno poslanstvo"
    )
    mission_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 2: URL do objavljenega dokumenta/podatkov",
    )
    has_published_key_employee_list = models.BooleanField(
        default=False,
        verbose_name="Kriterij 3: Organizacija ima objavljen seznam ključnih zaposlenih",
    )
    key_employee_list_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 3: URL do objavljenega dokumenta/podatkov",
    )
    has_published_board_member_list = models.BooleanField(
        default=False,
        verbose_name="Kriterij 4: Organizacija ima objavljen seznam članov nadzornih organov",
    )
    board_member_list_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 4: URL do objavljenega dokumenta/podatkov",
    )
    has_published_contact_information = models.BooleanField(
        default=False,
        verbose_name="Kriterij 5: Objavljen je način, kako lahko posameznik stopi v stik z organizacijo",
    )
    contact_information_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 5: URL do objavljenega dokumenta/podatkov",
    )
    has_published_complaints_contact = models.BooleanField(
        default=False,
        verbose_name="Kriterij 6: Objavljene so informacije o možnosti pritožbe nad delom organizacije s podatki komu/kako poslati pritožbe",
    )
    complaints_contact_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 6: URL do objavljenega dokumenta/podatkov",
    )
    has_published_complaints_process = models.BooleanField(
        default=False,
        verbose_name="Kriterij 7: Objavljen je celoten pritožbeni postopek",
    )
    complaints_process_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 7: URL do objavljenega dokumenta/podatkov",
    )

    # DOSTOPNOST VSEBINSKIH POROČIL
    has_published_substantive_report = models.BooleanField(
        default=False,
        verbose_name="Kriterij 1: Objavljeno je vsebinsko poročilo za preteklo leto",
    )
    substantive_report_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 1: URL do objavljenega dokumenta/podatkov",
    )
    has_published_report_about_work = models.BooleanField(
        default=False,
        verbose_name="Kriterij 2: Objavljeno je vsebinsko poročilo, iz katerega je jasno razvidno, s čim se organizacija ukvarja",
    )
    report_about_work_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 2: URL do objavljenega dokumenta/podatkov",
    )
    has_published_report_with_results = models.BooleanField(
        default=False,
        verbose_name="Kriterij 3: Vsebinsko poročilo vključuje tudi rezultate (dosežke, učinke), ne zgolj aktivnosti",
    )
    report_with_results_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 3: URL do objavljenega dokumenta/podatkov",
    )
    has_published_work_plan = models.BooleanField(
        default=False,
        verbose_name="Kriterij 4: Organizacija ima objavljen načrt dela za tekoče leto",
    )
    work_plan_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 4: URL do objavljenega dokumenta/podatkov",
    )
    has_published_strategic_objectives = models.BooleanField(
        default=False,
        verbose_name="Kriterij 5: Organizacija ima objavljene glavne strateške cilje",
    )
    strategic_objectives_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 5: URL do objavljenega dokumenta/podatkov",
    )

    # FINANČNA TRANSPARENTNOST
    has_published_financial_report = models.BooleanField(
        default=False,
        verbose_name="Kriterij 1: Organizacija ima objavljeno letno finančno poročilo za preteklo leto",
    )
    financial_report_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 1: URL do objavljenega dokumenta/podatkov",
    )
    has_published_understandable_financial_report = models.BooleanField(
        default=False,
        verbose_name="Kriterij 2: Finančna poročila so razdeljena po vrstah stroškov, ki so razumljiva javnosti (npr. stroški zaposlenih, potni stroški, stroški za zunanje izvajalce, itd.)",
    )
    understandable_financial_report_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 2: URL do objavljenega dokumenta/podatkov",
    )
    has_published_operating_expenses = models.BooleanField(
        default=False,
        verbose_name="Kriterij 3: Objavljen je podatek o višini ali odstotku sredstev, ki ga organizacija nameni za delovanje (hladni pogon)",
    )
    operating_expenses_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 3: URL do objavljenega dokumenta/podatkov",
    )
    has_published_main_sources_of_financing = models.BooleanField(
        default=False,
        verbose_name="Kriterij 4: Objavljeni so glavni viri financiranja (prihodki)",
    )
    main_sources_of_financing_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 4: URL do objavljenega dokumenta/podatkov",
    )
    has_published_management_revenues = models.BooleanField(
        default=False, verbose_name="Kriterij 5: Objavljeni so prihodki vodstva"
    )
    management_revenues_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 5: URL do objavljenega dokumenta/podatkov",
    )
    has_published_salary_ratio = models.BooleanField(
        default=False,
        verbose_name="Kriterij 6: Objavljeno je razmerje med najnižjo, povprečno in najvišjo plačo",
    )
    salary_ratio_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 6: URL do objavljenega dokumenta/podatkov",
    )

    # ZBIRANJE DONACIJSKIH SREDSTEV
    has_published_fundraising_reports = models.BooleanField(
        default=False,
        verbose_name="Kriterij 1: Objavljena so poročila o zbranih sredstvih",
    )
    fundraising_reports_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 1: URL do objavljenega dokumenta/podatkov",
    )
    has_published_fundraising_report_with_purposes = models.BooleanField(
        default=False,
        verbose_name="Kriterij 2: Poročilo o zbranih sredstvih je razdeljeno po namenih zbiranja (fundraising akcijah)",
    )
    fundraising_report_with_purposes_url = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Kriterij 2: URL do objavljenega dokumenta/podatkov",
    )

    # DOSTOP OBJAVLJENIH INFORMACIJ
    website_accessibility_contrast = models.BooleanField(
        default=False,
        verbose_name="Kriterij 1: Barvni kontrast med tekstom in ozadjem spletne strani je vsaj 4.5:1",
    )
    website_accessibility_zoom = models.BooleanField(
        default=False,
        verbose_name="Kriterij 2: Spletno mesto je berljivo tudi ob povečavi na 200 %",
    )
    website_accessibility_disabilities = models.BooleanField(
        default=False,
        verbose_name="Kriterij 3: Spletna stran je dostopna osebam z motoričnimi ali kognitivnimi ovirami",
    )

    # test_tuple_field = TupleField()

    def get_point_fields(self):
        return [
            field
            for field in self.__class__._meta.fields
            if isinstance(field, models.BooleanField)
            and (
                field.name.startswith("has_published_")
                or field.name.startswith("website_accessibility_")
            )
        ]

    def get_panel_tree(self):
        def panel_to_object(panel):
            if isinstance(panel, FieldPanel):
                return panel.field_name
            if isinstance(panel, InlinePanel):
                return panel.relation_name
            if isinstance(panel, MultiFieldPanel):
                return {
                    "name": panel.heading,
                    "children": [
                        panel_to_object(child_panel) for child_panel in panel.children
                    ],
                }
            return None

        return [
            panel_to_object(panel)
            for panel in self.__class__.panels
            if isinstance(panel, MultiFieldPanel)
        ]

    @property
    def stars(self):
        max_points = len(self.get_point_fields())
        points = self.points
        if points >= max_points * 0.9:
            return 5
        elif points >= max_points * 0.8:
            return 4
        elif points >= max_points * 0.7:
            return 3
        elif points >= max_points * 0.6:
            return 2
        elif points >= max_points * 0.5:
            return 1
        return 0

    @property
    def points(self):
        point_field_names = [field.name for field in self.get_point_fields()]
        return sum(list(map(lambda name: getattr(self, name, 0), point_field_names)))

    def compute_filtered_points(self, filter_keys):
        # TODO: fix
        return -1

    @property
    def points_details(self):
        point_fields = self.get_point_fields()
        panel_tree = self.get_panel_tree()

        def find_parent_panel(field_name):
            for panel in panel_tree:
                if isinstance(panel, dict):
                    for child in panel["children"]:
                        if isinstance(child, str) and child == field_name:
                            return panel["name"]
            return None

        def field_to_object(field):
            return {
                "section": find_parent_panel(field.name),
                "name": field.name,
                "verbose_name": field.verbose_name,
                "value": getattr(self, field.name, False),
            }

        return list(map(field_to_object, point_fields))

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
        # META INFO
        MultiFieldPanel(
            [
                HelpPanel(
                    heading="Povezava za urejanje",
                    template="wagtailadmin/edit_handlers/edit_key_panel.html",
                ),
                FieldPanel("is_complete"),
                FieldPanel("signup_time_start"),
                FieldPanel("signup_time"),
            ],
            heading="Podatki o prijavi",
        ),
        # OSEBNA IZKAZNICA ORGANIZACIJE
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("additional_names"),
                FieldPanel("cover_photo"),
                FieldPanel("address"),
                FieldPanel("contact_name"),
                FieldPanel("contact_email"),
                FieldPanel("contact_phone"),
                FieldPanel("tax_number"),
                FieldPanel("account_number"),
                FieldPanel("donation_url", widget=URLInputWithLink),
                FieldPanel("web_page", widget=URLInputWithLink),
                InlinePanel("links", label="Družbeni mediji"),
                FieldPanel("region", widget=CheckboxSelectMultiple),
                FieldPanel("area", widget=CheckboxSelectMultiple),
                FieldPanel("custom_area"),
            ],
            heading="Osebna izkaznica organizacije",
        ),
        # DOSTOPNOST OSNOVNIH INFORMACIJ
        MultiFieldPanel(
            [
                FieldPanel("has_published_key_documents"),
                FieldPanel("key_documents_url"),
                FieldPanel("has_published_mission"),
                FieldPanel("mission_url"),
                FieldPanel("has_published_key_employee_list"),
                FieldPanel("key_employee_list_url"),
                FieldPanel("has_published_board_member_list"),
                FieldPanel("board_member_list_url"),
                FieldPanel("has_published_contact_information"),
                FieldPanel("contact_information_url"),
                FieldPanel("has_published_complaints_contact"),
                FieldPanel("complaints_contact_url"),
                FieldPanel("has_published_complaints_process"),
                FieldPanel("complaints_process_url"),
            ],
            heading="Sklop 1: Dostopnost osnovnih informacij",
        ),
        # DOSTOPNOST VSEBINSKIH POROČIL
        MultiFieldPanel(
            [
                FieldPanel("has_published_substantive_report"),
                FieldPanel("substantive_report_url"),
                FieldPanel("has_published_report_about_work"),
                FieldPanel("report_about_work_url"),
                FieldPanel("has_published_report_with_results"),
                FieldPanel("report_with_results_url"),
                FieldPanel("has_published_work_plan"),
                FieldPanel("work_plan_url"),
                FieldPanel("has_published_strategic_objectives"),
                FieldPanel("strategic_objectives_url"),
            ],
            heading="Sklop 2: Dostopnost vsebinskih poročil",
        ),
        # FINANČNA TRANSPARENTNOST
        MultiFieldPanel(
            [
                FieldPanel("has_published_financial_report"),
                FieldPanel("financial_report_url"),
                FieldPanel("has_published_understandable_financial_report"),
                FieldPanel("understandable_financial_report_url"),
                FieldPanel("has_published_operating_expenses"),
                FieldPanel("operating_expenses_url"),
                FieldPanel("has_published_main_sources_of_financing"),
                FieldPanel("main_sources_of_financing_url"),
                FieldPanel("has_published_management_revenues"),
                FieldPanel("management_revenues_url"),
                FieldPanel("has_published_salary_ratio"),
                FieldPanel("salary_ratio_url"),
            ],
            heading="Sklop 3: Finančna transparentnost",
        ),
        # ZBIRANJE DONACIJSKIH SREDSTEV
        MultiFieldPanel(
            [
                FieldPanel("has_published_fundraising_reports"),
                FieldPanel("fundraising_reports_url"),
                FieldPanel("has_published_fundraising_report_with_purposes"),
                FieldPanel("fundraising_report_with_purposes_url"),
            ],
            heading="Sklop 4: Zbiranje donacijskih sredstev",
        ),
        # DOSTOP OBJAVLJENIH INFORMACIJ
        MultiFieldPanel(
            [
                FieldPanel("website_accessibility_contrast"),
                FieldPanel("website_accessibility_zoom"),
                FieldPanel("website_accessibility_disabilities"),
            ],
            heading="Sklop 5: Dostop objavljenih informacij",
        ),
        # REVIEW INFO
        MultiFieldPanel(
            [
                FieldPanel("review_date"),
                FieldPanel("review_notes"),
                FieldPanel("published"),
            ],
            heading="Podatki o pregledu",
        ),
        # FieldPanel("test_tuple_field", widget=LabeledTupleCheckboxes),
    ]

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Organizacija"
        verbose_name_plural = "Organizacije"


class Link(models.Model):
    organization = ParentalKey(
        "Organization",
        on_delete=models.CASCADE,
        related_name="links",
    )
    url = models.URLField(
        default="",
        blank=True,
        verbose_name="Povezava",
    )


class Area(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
