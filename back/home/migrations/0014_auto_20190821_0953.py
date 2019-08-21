# Generated by Django 2.2.3 on 2019-08-21 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20190821_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='has_milestiones_description',
            field=models.BooleanField(default=False, verbose_name='ali organizacija spremlja doseganje strateških ciljev?'),
        ),
        migrations.AddField(
            model_name='organization',
            name='has_strategic_goals',
            field=models.BooleanField(default=False, verbose_name='ima pisna poročila o spremljanju stateških ciljev?'),
        ),
    ]
