# Generated by Django 2.2.5 on 2019-10-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20190923_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='criteria',
            name='transparency_of_organizations_4_8',
            field=models.IntegerField(default=0, verbose_name='4.8 - Informacije so dostopne'),
        ),
    ]
