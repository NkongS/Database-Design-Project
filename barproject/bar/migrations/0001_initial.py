# Generated by Django 5.0.3 on 2024-03-29 03:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BarInventory',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, max_length=30, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bar_inventory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bartables',
            fields=[
                ('table_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('check_out_time', models.TimeField(blank=True, null=True)),
                ('table_status', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bartables',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_name', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'branches',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeePosition',
            fields=[
                ('position_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('position_name', models.CharField(blank=True, max_length=30, null=True)),
                ('min_salary', models.IntegerField(blank=True, null=True)),
                ('max_salary', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employee_position',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employee_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_info', models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True)),
                ('email', models.CharField(blank=True, max_length=45, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('hire_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeSchedules',
            fields=[
                ('schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('shift_start', models.TimeField(blank=True, null=True)),
                ('shift_end', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'employee_schedules',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FeedbackReviews',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('feedbacks', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'feedback_reviews',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('address_no', models.CharField(blank=True, max_length=40, null=True)),
                ('street_name', models.CharField(blank=True, max_length=30, null=True)),
                ('city_name', models.CharField(max_length=30)),
                ('province_name', models.CharField(blank=True, max_length=25, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=12, null=True)),
                ('country_name', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'locations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('membership_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('second_name', models.CharField(blank=True, max_length=30, null=True)),
                ('contact_info', models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True)),
                ('membership_status', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'membership',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('reservation_time', models.TimeField(blank=True, null=True)),
                ('number_of_guests', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'reservations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SecurityLogs',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('log_time', models.TimeField(blank=True, null=True)),
                ('activity_log', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'security_logs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Guesses',
            fields=[
                ('branch', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='bar.branches')),
                ('guess_first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('guess_last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('guess_band', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'guesses',
                'managed': False,
            },
        ),
    ]
