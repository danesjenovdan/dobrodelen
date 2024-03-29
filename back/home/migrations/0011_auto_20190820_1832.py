# Generated by Django 2.2.3 on 2019-08-20 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20190808_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='name',
        ),
        migrations.AlterField(
            model_name='organization',
            name='custom_area',
            field=models.TextField(blank=True, default='', verbose_name='Področje delovanja Other'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='is_complete',
            field=models.BooleanField(default=False, verbose_name='Je končan'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Je objavlen'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='zero5',
            field=models.BooleanField(blank=True, default=False, verbose_name='Organizacija je na seznamu upravičencev do 0,5 dohodnine'),
        ),
    ]
