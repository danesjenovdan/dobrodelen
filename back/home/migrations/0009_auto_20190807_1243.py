# Generated by Django 2.2.3 on 2019-08-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_organization_custom_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='contact_info',
        ),
        migrations.AddField(
            model_name='organization',
            name='contact_email',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='Kontakt: e-pošta'),
        ),
        migrations.AddField(
            model_name='organization',
            name='contact_name',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='Kontakt: ime in priimek'),
        ),
        migrations.AddField(
            model_name='organization',
            name='contact_phone',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='Kontakt: telefon'),
        ),
    ]