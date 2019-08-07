from django.db import models
from django.core import signing
from modelcluster.models import ClusterableModel, ParentalKey
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


def get_intance_path(instance, file_name):
    return 'documents/{}/{}'.format(
        instance.pk,
        file_name)


class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        context["organizations"] = Organization.objects.filter(published=True)
        return context


class Organization(ClusterableModel):
    name = models.CharField(max_length=512, default="",
                            verbose_name="Uradno ime organizacije (iz AJPES)", blank=True)
    additional_names = models.TextField(
        verbose_name="Druga imena, pod katerimi je organizacija poznana (kratice, okrajšave)", default='', blank=True)
    contact_name = models.CharField(
        verbose_name="Kontakt: ime in priimek", default='', blank=True, max_length=128)
    contact_email = models.CharField(
        verbose_name="Kontakt: e-pošta", default='', blank=True, max_length=128)
    contact_phone = models.CharField(
        verbose_name="Kontakt: telefon", default='', blank=True, max_length=128)
    web_page = models.URLField(
        max_length=512, verbose_name='spletna stran', default='', blank=True)
    description = models.TextField(
        verbose_name='kratek opis organizacije (do 1500 znakov)', default='', blank=True)
    tax_number = models.CharField(
        max_length=32, verbose_name='davčna številka', default='', blank=True)
    mission = models.TextField(
        verbose_name='Poslanstvo organizacije (do 500 znakov)', default='', blank=True)
    area = models.ManyToManyField('Area', blank=True, related_name='organization',
                                  verbose_name='Področje delovanja (lahko izberete več možnosti)', default='')
    custom_area = models.TextField(verbose_name='Področje delovanja Other', default='')
    avg_revenue = models.CharField(
        max_length=16, verbose_name='povprečni letni proračun v zadnjih treh letih', default='', blank=True)
    employed = models.IntegerField(
        verbose_name='število zaposlenih v zadnjem zaključenem letu', default=0, blank=True)
    is_charity = models.BooleanField(
        default=False, verbose_name='Organizacija ima status humanitarne organizacije', blank=True)
    has_public_interest = models.BooleanField(
        default=False, verbose_name='Organizacija ima status delovanja v javnem interesu', blank=True)
    is_voluntary = models.BooleanField(
        default=False, verbose_name='Organizacija je vpisana v evidenco prostotovoljskih organizacij', blank=True)
    zero5 = models.BooleanField(
        default=False, verbose_name='Organizacija je na seznamu upravičencev do 0,5 % dohodnine', blank=True)

    board_members = ParentalManyToManyField(
        'Member', related_name='organization_supervisor', blank=True, through='BoardMember')

    strategic_planning = models.BooleanField(
        default=False, verbose_name='Ali organizacija strateško načrtuje?')
    milestiones_description = models.TextField(
        verbose_name='ali organizacija spremlja doseganje strateških ciljev? -> kratek opis kako, max 500 znakov', default='', blank=True)
    wages_ratio = models.TextField(
        verbose_name="razmerje med najvišjo in povprečno plačo v organizaciji", default='', blank=True)

    # documents
    minutes_meeteng = models.FileField(
        upload_to=get_intance_path, verbose_name='priloga zapisnik zadnje seje', blank=True, null=True)
    strategic_goals = models.FileField(
        upload_to=get_intance_path, verbose_name='pisna poročila o spremljanju stateških ciljev', blank=True, null=True)
    finance_report = models.FileField(
        upload_to=get_intance_path, verbose_name='Finančno poročilo', blank=True, null=True)
    finance_report_ajpes = models.FileField(
        upload_to=get_intance_path, verbose_name='finančno poročilo, ki je bilo oddano na AJPES', blank=True, null=True)
    audited_report = models.FileField(
        upload_to=get_intance_path, verbose_name='revidirano poročilo', blank=True, null=True)
    finance_plan = models.FileField(
        upload_to=get_intance_path, verbose_name='finančni načrt za tekoče leto', blank=True, null=True)
    given_loan = models.FileField(
        upload_to=get_intance_path, verbose_name='seznam danih posojil', blank=True, null=True)
    received_loans = models.FileField(
        upload_to=get_intance_path, verbose_name='seznam prejetih posojil', blank=True, null=True)
    payment_classes = models.FileField(
        upload_to=get_intance_path, verbose_name='akt o sistematizaciji delovnih mest in plačnih razredov', blank=True, null=True)

    cover_photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    published = models.BooleanField(default=False, verbose_name='')
    signup_time = models.DateTimeField(auto_now_add=True, verbose_name='')

    @property
    def stars(self):
        if self.criteria and self.criteria.count() > 0:
            return self.criteria.first().stars
        return -1

    @property
    def edit_key(self):
        return signing.dumps(self.pk, salt="ORG_EDIT_KEY")

    panels = [
        FieldPanel("name"),
        FieldPanel("additional_names"),
        FieldPanel("contact_name"),
        FieldPanel("contact_email"),
        FieldPanel("contact_phone"),
        FieldPanel("web_page"),
        FieldPanel("description"),
        FieldPanel("tax_number"),
        FieldPanel("mission"),
        FieldPanel("area"),
        FieldPanel("avg_revenue"),
        FieldPanel("employed"),
        FieldPanel("is_charity"),
        FieldPanel("has_public_interest"),
        FieldPanel("is_voluntary"),
        FieldPanel("zero5"),
        FieldPanel("strategic_planning"),
        FieldPanel("milestiones_description"),
        FieldPanel("wages_ratio"),
        FieldPanel("minutes_meeteng"),
        FieldPanel("strategic_goals"),
        FieldPanel("finance_report"),
        FieldPanel("finance_report_ajpes"),
        FieldPanel("audited_report"),
        FieldPanel("finance_plan"),
        FieldPanel("given_loan"),
        FieldPanel("received_loans"),
        FieldPanel("payment_classes"),
        FieldPanel("published"),
        ImageChooserPanel("cover_photo"),
        #InlinePanel("boards", label="Boards"),
        InlinePanel("memberships", label="Memberships"),
        InlinePanel("links", label="Links"),
        InlinePanel("documents", label="Documents"),
        InlinePanel(
            "criteria", label="Criteria", classname="criteria_panel", max_num=1
        ),
    ]

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Organizacija"
        verbose_name_plural = "Organizacije"


class Member(ClusterableModel):
    name = models.CharField(max_length=512, default="",
                            verbose_name="Ime in priimek")
    role = models.CharField(max_length=512, default="",
                            verbose_name="povezava z organizacijo")


class Board(ClusterableModel):
    name = models.CharField(max_length=256)
    meeting_dates = models.TextField(blank=True, default='')

    organization = ParentalKey(
        'Organization', related_name='boards', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name + ' --> ' + str(self.organization.name) if self.organization else ''


class BoardMember(models.Model):
    board = ParentalKey(
        'Board', related_name='memberships', on_delete=models.CASCADE, null=True)
    member = ParentalKey(
        'Member', related_name='memberships', on_delete=models.CASCADE, null=True)
    organization = ParentalKey(
        'Organization', related_name='memberships', on_delete=models.CASCADE, null=True)
    is_paid = models.BooleanField(
        default=False, verbose_name='Ali za svoje delo v odboru prejema nadomestilo')

    def __str__(self):
        return str(self.member.name) if self.member else '' + \
            '->' + str(self.member.organization.name) if self.member.organization.name else '' + \
            '->' + str(self.member.board.name) if self.member.board.anme else ''


class Link(models.Model):
    name = models.CharField(max_length=512, default="")
    url = models.URLField()
    organization = ParentalKey(
        "Organization", on_delete=models.CASCADE, related_name="links"
    )


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
        default=0,
        verbose_name="4.2 - Letna poročila o delu so razumljiva"
    )
    transparency_of_organizations_4_2_1 = models.IntegerField(
        default=0,
        verbose_name="4.2.1 - Organizacija ima objavljena letna finančna poročila",
    )
    transparency_of_organizations_4_2_2 = models.IntegerField(
        default=0,
        verbose_name="4.2.2 - Finančna poročila so razumljiva"
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


class DocumentAttachment(models.Model):
    name = models.CharField(max_length=512)
    file = models.FileField(upload_to="documents/")
    organization = ParentalKey(
        "Organization", on_delete=models.CASCADE, related_name="documents"
    )


class Area(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name