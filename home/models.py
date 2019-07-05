from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    pass


class Organization(models.Model):
    name = models.CharField(max_length=512, default='')
    description = models.TextField()
    published = models.BooleanField(default=False)
    criterions = models.OneToOneField('Criterion', on_delete=models.CASCADE)


class Link(models.Model):
    name = models.CharField(max_length=512, default='')
    url = models.URLField()
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)


class Criterion(models.Model):
    control_of_business_1 = models.IntegerField(
        default=0,
        verbose_name='število sestankov nadzornega/upravnega odbora v zadnjem letu'
    )
    control_of_business_2 = models.IntegerField(
        default=0,
        verbose_name='število neodvisnih članov nadzornega/upravnega odbora, ki ima glasovalno pravico'
    )
    control_of_business_3 = models.IntegerField(
        default=0,
        verbose_name='odstotek neodvisnih članov z glasovalno pravico'
    )
    control_of_business_4 = models.IntegerField(
        default=0,
        verbose_name='organizacija ima zapisnike sej'
    )

    strategic_planning_2_1 = models.IntegerField(
        default=0,
        verbose_name='organizacija ima strateški načrt'
    )
    strategic_planning_2_2 = models.IntegerField(
        default=0,
        verbose_name='organizacija spremlja doseganje strateškega načrta'
    )
    strategic_planning_2_3 = models.IntegerField(
        default=0,
        verbose_name='organizacija pripravlja poročila o spremljanju napredka pri doseganju strateških ciljev'
    )

    financial_management_3_1 = models.IntegerField(
        default=0,
        verbose_name='odstotek sredstev, ki jih porabi za izvedbo programa'
    )
    financial_management_3_2 = models.IntegerField(
        default=0,
        verbose_name='odstotek sredstev, ki jh organizacija porabi za splošno delovanje'
    )
    financial_management_3_3 = models.IntegerField(
        default=0,
        verbose_name='znesek, ki ga organizacija porabi na vsakih zbranih 100 €'
    )
    financial_management_3_4_1 = models.IntegerField(
        default=0,
        verbose_name='viri sredstev'
    )
    financial_management_3_4_2 = models.IntegerField(
        default=0,
        verbose_name='delež prihodkov iz navečjega posameznega vira'
    )
    financial_management_3_5_1 = models.IntegerField(
        default=0,
        verbose_name='organizacija daje posojila povezanim osebam'
    )
    financial_management_3_5_2 = models.IntegerField(
        default=0,
        verbose_name='organizacija prejema posojila od povezanih oseb'
    )
    financial_management_3_6 = models.IntegerField(
        default=0,
        verbose_name='razmerje med najvišjo in povprečno plačo v organizaciji'
    )

    transparency_of_organizations_4_1 = models.IntegerField(
        default=0,
        verbose_name='organizacija ima objavljena letna poročila o delu'
    )
    transparency_of_organizations_4_2 = models.IntegerField(
        default=0,
        verbose_name='letna poročila o delu so razumljiva'
    )
    transparency_of_organizations_4_2_1 = models.IntegerField(
        default=0,
        verbose_name='organizacija ima objavljena letna finančna poročila'
    )
    transparency_of_organizations_4_2_2 = models.IntegerField(
        default=0,
        verbose_name='finančna poročila so razumljiva'
    )
    transparency_of_organizations_4_2_3 = models.IntegerField(
        default=0,
        verbose_name='finančna poročila so razdeljena po programih in vrstah stroškov in prihodkov'
    )
    transparency_of_organizations_4_3 = models.IntegerField(
        default=0,
        verbose_name='Objavljene so plače vodstva'
    )
    transparency_of_organizations_4_4 = models.IntegerField(
        default=0,
        verbose_name='objavljeno je razmerje med plačami'
    )
    transparency_of_organizations_4_5 = models.IntegerField(
        default=0,
        verbose_name='objavljen je seznam ključnih zaposlenih'
    )
    transparency_of_organizations_4_6 = models.IntegerField(
        default=0,
        verbose_name='obljavljeni so člani nadzornega/upravnega odbora'
    )
    transparency_of_organizations_4_7 = models.IntegerField(
        default=0,
        verbose_name='objavljen je finančni načrt za tekoče leto'
    )


class Attachment(models.Model):
    organization = models.ForeignKey(
        'Organization',
        on_delete=models.CASCADE,
        related_name='attachments'
    )
    name = models.CharField(max_length=512)
    file = models.FileField(upload_to='documents/')