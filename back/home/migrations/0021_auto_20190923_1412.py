# Generated by Django 2.2.5 on 2019-09-23 12:12

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20190923_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouncilBoardMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=512, verbose_name='Ime in priimek')),
                ('role', models.CharField(choices=[('1', 'Član'), ('2', 'Predstavnik uporabnikov'), ('3', 'Predstavnik zaposlenih'), ('4', 'Predstavnik ustanoviteljev'), ('5', 'Imenovan na podlagi sorodstvenih/prijateljskih vezi'), ('6', 'Neodvisni predstavnik'), ('7', 'Drugo:')], default='1', max_length=2)),
                ('custom_role', models.CharField(blank=True, default='', max_length=128, verbose_name='Povezava z organizacijo: Drugo')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Ali za svoje delo v odboru prejema nadomestilo')),
            ],
        ),
        migrations.CreateModel(
            name='ManagementBoardMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=512, verbose_name='Ime in priimek')),
                ('role', models.CharField(choices=[('1', 'Član'), ('2', 'Predstavnik uporabnikov'), ('3', 'Predstavnik zaposlenih'), ('4', 'Predstavnik ustanoviteljev'), ('5', 'Imenovan na podlagi sorodstvenih/prijateljskih vezi'), ('6', 'Neodvisni predstavnik'), ('7', 'Drugo:')], default='1', max_length=2)),
                ('custom_role', models.CharField(blank=True, default='', max_length=128, verbose_name='Povezava z organizacijo: Drugo')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Ali za svoje delo v odboru prejema nadomestilo')),
            ],
        ),
        migrations.CreateModel(
            name='OtherBoardMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=512, verbose_name='Ime in priimek')),
                ('role', models.CharField(choices=[('1', 'Član'), ('2', 'Predstavnik uporabnikov'), ('3', 'Predstavnik zaposlenih'), ('4', 'Predstavnik ustanoviteljev'), ('5', 'Imenovan na podlagi sorodstvenih/prijateljskih vezi'), ('6', 'Neodvisni predstavnik'), ('7', 'Drugo:')], default='1', max_length=2)),
                ('custom_role', models.CharField(blank=True, default='', max_length=128, verbose_name='Povezava z organizacijo: Drugo')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Ali za svoje delo v odboru prejema nadomestilo')),
            ],
        ),
        migrations.CreateModel(
            name='SupervisoryBoardMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=512, verbose_name='Ime in priimek')),
                ('role', models.CharField(choices=[('1', 'Član'), ('2', 'Predstavnik uporabnikov'), ('3', 'Predstavnik zaposlenih'), ('4', 'Predstavnik ustanoviteljev'), ('5', 'Imenovan na podlagi sorodstvenih/prijateljskih vezi'), ('6', 'Neodvisni predstavnik'), ('7', 'Drugo:')], default='1', max_length=2)),
                ('custom_role', models.CharField(blank=True, default='', max_length=128, verbose_name='Povezava z organizacijo: Drugo')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Ali za svoje delo v odboru prejema nadomestilo')),
            ],
        ),
        migrations.RemoveField(
            model_name='organization',
            name='council_members',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='management_board_members',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='other_board_members',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='supervisory_board_members',
        ),
        migrations.DeleteModel(
            name='BoardMember',
        ),
        migrations.AddField(
            model_name='supervisoryboardmember',
            name='organization',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='supervisory_board_members', to='home.Organization'),
        ),
        migrations.AddField(
            model_name='otherboardmember',
            name='organization',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_board_members', to='home.Organization'),
        ),
        migrations.AddField(
            model_name='managementboardmember',
            name='organization',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='management_board_members', to='home.Organization'),
        ),
        migrations.AddField(
            model_name='councilboardmember',
            name='organization',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='council_members', to='home.Organization'),
        ),
    ]
