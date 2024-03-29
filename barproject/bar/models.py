# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BarInventory(models.Model):
    product_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey('Branches', models.DO_NOTHING, blank=True, null=True)
    product_name = models.CharField(max_length=30, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bar_inventory'


class Bartables(models.Model):
    branch = models.ForeignKey('Branches', models.DO_NOTHING, blank=True, null=True)
    table_id = models.CharField(primary_key=True, max_length=8)
    start_time = models.TimeField(blank=True, null=True)
    check_out_time = models.TimeField(blank=True, null=True)
    table_status = models.BooleanField(blank=True, null=True)
    reservation = models.ForeignKey('Reservations', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bartables'


class Branches(models.Model):
    branch_id = models.AutoField(primary_key=True)
    location = models.ForeignKey('Locations', models.DO_NOTHING, blank=True, null=True)
    branch_name = models.CharField(max_length=40, blank=True, null=True)
    employee = models.ForeignKey('Employees', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branches'


class EmployeePosition(models.Model):
    position_id = models.CharField(primary_key=True, max_length=10)
    position_name = models.CharField(max_length=30, blank=True, null=True)
    min_salary = models.IntegerField(blank=True, null=True)
    max_salary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_position'


class EmployeeSchedules(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branches, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey('Employees', models.DO_NOTHING, blank=True, null=True)
    shift_start = models.TimeField(blank=True, null=True)
    shift_end = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_schedules'


class Employees(models.Model):
    employee_id = models.CharField(primary_key=True, max_length=10)
    position = models.ForeignKey(EmployeePosition, models.DO_NOTHING, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    contact_info = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    branch = models.ForeignKey(Branches, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class FeedbackReviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    membership = models.ForeignKey('Membership', models.DO_NOTHING, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    feedbacks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback_reviews'


class Guesses(models.Model):
    branch = models.OneToOneField(Branches, models.DO_NOTHING, primary_key=True)
    table = models.ForeignKey(Bartables, models.DO_NOTHING)
    guess_first_name = models.CharField(max_length=30, blank=True, null=True)
    guess_last_name = models.CharField(max_length=30, blank=True, null=True)
    guess_band = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guesses'
        unique_together = (('branch', 'table'),)


class Locations(models.Model):
    location_id = models.AutoField(primary_key=True)
    address_no = models.CharField(max_length=40, blank=True, null=True)
    street_name = models.CharField(max_length=30, blank=True, null=True)
    city_name = models.CharField(max_length=30)
    province_name = models.CharField(max_length=25, blank=True, null=True)
    postal_code = models.CharField(max_length=12, blank=True, null=True)
    country_name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'
    def __str__(self):
        return self.city_name

class Membership(models.Model):
    membership_id = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    second_name = models.CharField(max_length=30, blank=True, null=True)
    contact_info = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    membership_status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membership'


class Reservations(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branches, models.DO_NOTHING, blank=True, null=True)
    table = models.ForeignKey(Bartables, models.DO_NOTHING, blank=True, null=True)
    membership = models.ForeignKey(Membership, models.DO_NOTHING, blank=True, null=True)
    reservation_time = models.TimeField(blank=True, null=True)
    number_of_guests = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservations'


class SecurityLogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branches, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING, blank=True, null=True)
    log_time = models.TimeField(blank=True, null=True)
    activity_log = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'security_logs'
