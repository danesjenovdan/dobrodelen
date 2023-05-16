# Generated by Django 4.1.5 on 2023-01-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0032_delete_criteria"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="organization",
            name="audited_report",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="council_dates",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="finance_plan",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="finance_report",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="finance_report_ajpes",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="given_loan",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_audited_report",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_council",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_finance_plan",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_given_loans",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_management_board",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_milestiones_description",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_minutes_meeting",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_other_board",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_payment_classes",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_published_board_members",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_published_employee_list",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_published_executive_salaries",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_published_financial_plan",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_published_financial_reports",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_published_salary_ratio",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_published_work_reports",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_received_loans",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_strategic_goals",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="has_supervisory_board",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="management_board_dates",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="milestiones_description",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="minutes_meeting",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="mission",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="other_board_dates",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="other_board_name",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="payment_classes",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="published_board_members_url",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="published_employee_list_url",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="published_executive_salaries_url",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="published_financial_plan_url",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="published_financial_reports_url",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="published_salary_ratio_url",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="published_work_reports_url",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="received_loans",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="strategic_goals",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="strategic_planning",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="supervisory_board_dates",
        ),
        migrations.RemoveField(
            model_name="organization",
            name="wages_ratio",
        ),
        migrations.AddField(
            model_name="organization",
            name="zero5_amount",
            field=models.IntegerField(
                blank=True,
                default=0,
                verbose_name="Višina zbranih sredstev prek 1 % dohodnine",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="description",
            field=models.TextField(
                blank=True,
                default="",
                verbose_name="Kratek opis organizacije (do 500 znakov)",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="zero5",
            field=models.BooleanField(
                blank=True,
                default=False,
                verbose_name="Organizacija je na seznamu upravičencev do 1 % dohodnine",
            ),
        ),
    ]