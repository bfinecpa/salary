# Generated by Django 3.1.3 on 2021-02-25 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Go',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.TextField()),
                ('name', models.CharField(max_length=4)),
                ('Code', models.TextField()),
                ('total_payment', models.TextField(blank=True, null=True)),
                ('total_deduction', models.TextField(blank=True, null=True)),
                ('actual_payment', models.TextField(blank=True, null=True)),
                ('last_payment', models.TextField(blank=True, null=True)),
                ('other_salary', models.TextField(blank=True, null=True)),
                ('meals', models.TextField(blank=True, null=True)),
                ('maternity_leave', models.TextField(blank=True, null=True)),
                ('Incentive', models.TextField(blank=True, null=True)),
                ('payroll', models.TextField(blank=True, null=True)),
                ('school_expenses', models.TextField(blank=True, null=True)),
                ('license_allowance', models.TextField(blank=True, null=True)),
                ('overtime_allowance', models.TextField(blank=True, null=True)),
                ('duty_allowance', models.TextField(blank=True, null=True)),
                ('annual_allowance', models.TextField(blank=True, null=True)),
                ('other_allowance', models.TextField(blank=True, null=True)),
                ('long_term_reward', models.TextField(blank=True, null=True)),
                ('RSP', models.TextField(blank=True, null=True)),
                ('allowance', models.TextField(blank=True, null=True)),
                ('resident_tax', models.TextField(blank=True, null=True)),
                ('tax_meter', models.TextField(blank=True, null=True)),
                ('health_insurance_premium', models.TextField(blank=True, null=True)),
                ('employment_insurance_premium', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_name', models.TextField(blank=True, default='')),
                ('employee_number', models.TextField(blank=True, default='')),
                ('name', models.CharField(blank=True, max_length=4, null=True)),
                ('employee_code', models.TextField(blank=True, default='')),
                ('total_payment', models.TextField(blank=True, default='')),
                ('total_deduction', models.TextField(blank=True, default='')),
                ('actual_payment', models.TextField(blank=True, default='')),
                ('entered_date', models.TextField(blank=True, default='')),
                ('salary_step', models.TextField(blank=True, default='')),
                ('rank', models.TextField(blank=True, default='')),
                ('department', models.TextField(blank=True, default='')),
                ('normal', models.TextField(blank=True, default='')),
                ('holiday_subsidy', models.TextField(blank=True, default='')),
                ('incentive', models.TextField(blank=True, default='')),
                ('other_salary_settlement', models.TextField(blank=True, default='')),
                ('school_expenses', models.TextField(blank=True, default='')),
                ('license_allowance', models.TextField(blank=True, default='')),
                ('overtime_allowance', models.TextField(blank=True, default='')),
                ('duty_allowance', models.TextField(blank=True, default='')),
                ('annual_allowance', models.TextField(blank=True, default='')),
                ('long_term_reward', models.TextField(blank=True, default='')),
                ('other_allowance', models.TextField(blank=True, default='')),
                ('other_salary_payments', models.TextField(blank=True, default='')),
                ('maternity_leave', models.TextField(blank=True, default='')),
                ('meals', models.TextField(blank=True, default='')),
                ('national_pension', models.TextField(blank=True, default='')),
                ('health_insurance_premium', models.TextField(blank=True, default='')),
                ('employment_insurance', models.TextField(blank=True, default='')),
                ('long_term_care_premium', models.TextField(blank=True, default='')),
                ('income_tax', models.TextField(blank=True, default='')),
                ('local_income_tax', models.TextField(blank=True, default='')),
                ('Year_end_settlement_income_tax', models.TextField(blank=True, default='')),
                ('local_income_tax_for_year_end_settlement', models.TextField(blank=True, default='')),
                ('year_and_settlement_agricultural_special_tax', models.TextField(blank=True, default='')),
                ('membership_fee', models.TextField(blank=True, default='')),
                ('repayment_of_hosing_funds', models.TextField(blank=True, default='')),
                ('other_one', models.TextField(blank=True, default='')),
                ('other_two', models.TextField(blank=True, default='')),
                ('health_insurance_premium_settlement', models.TextField(blank=True, default='')),
                ('long_term_care_premium_settlement', models.TextField(blank=True, default='')),
            ],
        ),
    ]
