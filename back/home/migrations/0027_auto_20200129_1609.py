# Generated by Django 2.2.5 on 2020-01-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20200129_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='region',
            field=models.ManyToManyField(blank=True, default='', related_name='organization', to='home.Region', verbose_name='Regije (lahko izberete več možnosti)'),
        ),
    ]
