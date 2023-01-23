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
    # info
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
    # org info
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
    description = models.TextField(
        default="",
        blank=True,
        verbose_name="Kratek opis organizacije (do 500 znakov)",
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
    web_page = models.URLField(
        max_length=512,
        default="",
        blank=True,
        verbose_name="Spletna stran",
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
    avg_revenue = models.IntegerField(
        default=0,
        blank=True,
        verbose_name="Povprečni letni proračun v zadnjih treh letih",
    )
    employed = models.IntegerField(
        default=0,
        blank=True,
        verbose_name="Število zaposlenih v zadnjem zaključenem letu",
    )
    is_charity = models.BooleanField(
        default=False,
        blank=True,
        verbose_name="Organizacija ima status humanitarne organizacije",
    )
    has_public_interest = models.BooleanField(
        default=False,
        blank=True,
        verbose_name="Organizacija ima status delovanja v javnem interesu",
    )
    is_voluntary = models.BooleanField(
        default=False,
        blank=True,
        verbose_name="Organizacija je vpisana v evidenco prostovoljskih organizacij",
    )
    zero5 = models.BooleanField(
        default=False,
        blank=True,
        verbose_name="Organizacija je na seznamu upravičencev do 1 % dohodnine",
    )
    zero5_amount = models.IntegerField(
        default=0,
        blank=True,
        verbose_name="Višina zbranih sredstev prek 1 % dohodnine",
    )
    region = models.ManyToManyField(
        "Region",
        default="",
        blank=True,
        related_name="organization",
        verbose_name="Regije (lahko izberete več možnosti)",
    )
    # criteria
    # - test_tuple_field = TupleField()
    # review
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

    @property
    def stars(self):
        # TODO: fix
        return -1

    @property
    def points(self):
        # TODO: fix
        return -1

    def compute_filtered_points(self, filter_keys):
        # TODO: fix
        # criteria = self.criteria.first()
        # if criteria:
        #     fields = [
        #         field
        #         for field in Criteria._meta.fields
        #         if field.name not in ["id", "organization", "stars", "points"]
        #         and field.verbose_name.split(" - ")[0] in filter_keys
        #     ]
        #     return sum(
        #         list(map(lambda field: getattr(criteria, field.name, 0), fields))
        #     )
        return -1

    @property
    def points_details(self):
        # TODO: fix
        # criteria = self.criteria.first()
        fields = [
            # field
            # for field in Criteria._meta.fields
            # if field.name not in ["id", "organization", "stars", "points"]
        ]

        def field_to_object(field):
            return {
                # "name": field.name,
                # "verbose_name": field.verbose_name,
                # "value": getattr(criteria, field.name, 0),
                # "max_value": Criteria.max_values.get(
                #     field.verbose_name.split(" - ")[0], 0
                # ),
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
        # info
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
        # org info
        FieldPanel("name"),
        FieldPanel("additional_names"),
        FieldPanel("description"),
        FieldPanel("address"),
        FieldPanel("contact_name"),
        FieldPanel("contact_email"),
        FieldPanel("contact_phone"),
        FieldPanel("web_page", widget=URLInputWithLink),
        InlinePanel("links", label="Družbeni mediji"),
        FieldPanel("cover_photo"),
        FieldPanel("tax_number"),
        FieldPanel("account_number"),
        FieldPanel("donation_url", widget=URLInputWithLink),
        FieldPanel("area", widget=CheckboxSelectMultiple),
        FieldPanel("custom_area"),
        FieldPanel("avg_revenue"),
        FieldPanel("employed"),
        FieldPanel("is_charity"),
        FieldPanel("has_public_interest"),
        FieldPanel("is_voluntary"),
        FieldPanel("zero5"),
        FieldPanel("zero5_amount"),
        FieldPanel("region", widget=CheckboxSelectMultiple),
        # criteria
        # FieldPanel("test_tuple_field", widget=LabeledTupleCheckboxes),
        # review
        MultiFieldPanel(
            [
                FieldPanel("review_date"),
                FieldPanel("review_notes"),
                FieldPanel("published"),
            ],
            heading="Podatki o pregledu",
        ),
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
