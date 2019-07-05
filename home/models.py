from django.db import models
from modelcluster.models import ClusterableModel, ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        context["organizations"] = Organization.objects.filter(published=True)
        return context


class Organization(ClusterableModel):
    name = models.CharField(max_length=512, default="")
    description = models.TextField()
    published = models.BooleanField(default=False)
    cover_photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("published"),
        ImageChooserPanel("cover_photo"),
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


class DocumentAttachment(models.Model):
    name = models.CharField(max_length=512)
    file = models.FileField(upload_to="documents/")
    organization = ParentalKey(
        "Organization", on_delete=models.CASCADE, related_name="documents"
    )
