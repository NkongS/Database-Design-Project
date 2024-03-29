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
    def __str__(self):
        if self.branch:
            return f"Branch: {self.branch.branch_id}, {self.product_name}, Quantity: {self.quantity}, Price: {self.price}"
        else:
            return f"Product ID: {self.product_id}, {self.product_name}, Quantity: {self.quantity}, Price: {self.price}"



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
    def __str__(self):
        table_str = f"Table ID: {self.table_id}, Branch ID: {self.branch.branch_id}, Status: {self.table_status}"
        return table_str


class Branches(models.Model):
    branch_id = models.AutoField(primary_key=True)
    location = models.ForeignKey('Locations', models.DO_NOTHING, blank=True, null=True)
    branch_name = models.CharField(max_length=40, blank=True, null=True)
    employee = models.ForeignKey('Employees', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branches'
    def __str__(self):
        branch_str = f"Branch: {self.branch_id}, {self.branch_name}, {self.location}"
        return branch_str


class EmployeePosition(models.Model):
    position_id = models.CharField(primary_key=True, max_length=10)
    position_name = models.CharField(max_length=30, blank=True, null=True)
    min_salary = models.IntegerField(blank=True, null=True)
    max_salary = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_position'
    def __str__(self):
        position_str = f"Position ID: {self.position_id}, {self.position_name}, Salary: {self.min_salary} - {self.max_salary}"
        return position_str


class EmployeeSchedules(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branches, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey('Employees', models.DO_NOTHING, blank=True, null=True)
    shift_start = models.TimeField(blank=True, null=True)
    shift_end = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_schedules'
    def __str__(self):
        schedule_str = f"Schedule ID: {self.schedule_id}, Branch: {self.branch}, Employee: {self.employee}, Shift: {self.shift_start} - {self.shift_end}"
        return schedule_str


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
    def __str__(self):
        employee_str = f"Branch: {self.branch.branch_id}, Employee ID: {self.employee_id}, {self.first_name} {self.last_name}, {self.position.position_name}, {self.salary}"
        return employee_str


class FeedbackReviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    membership = models.ForeignKey('Membership', models.DO_NOTHING, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    feedbacks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedback_reviews'
    def __str__(self):
        review_str = f"Review ID: {self.review_id}, Membership: {(self.membership.membership_id if self.membership else 'None')}, Rating: {self.rating}"
        return review_str


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
    def __str__(self):
        guess_str = f"Branch: {self.branch}, Table: {self.table}, {self.guess_first_name} {self.guess_last_name}, Band: {self.guess_band}"
        return guess_str


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
        location_str = f"Location ID: {self.location_id}, {self.city_name}, {self.country_name}"
        return location_str

class Membership(models.Model):
    membership_id = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    second_name = models.CharField(max_length=30, blank=True, null=True)
    contact_info = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    membership_status = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'membership'
    def __str__(self):
        membership_str = f"Membership ID: {self.membership_id}, {self.first_name} {self.second_name}, Status: {self.membership_status}"
        return membership_str


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
    def __str__(self):
        reservation_str = f"Reservation ID: {self.reservation_id}, Branch: {self.branch}, Table: {self.table}, Membership: {self.membership}, Time: {self.reservation_time}, Guests: {self.number_of_guests}"
        return reservation_str


class SecurityLogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branches, models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING, blank=True, null=True)
    log_time = models.TimeField(blank=True, null=True)
    activity_log = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'security_logs'
    def __str__(self):
        log_str = f"Log ID: {self.log_id}, Branch: {self.branch}, Employee: {self.employee}, Time: {self.log_time}, Activity: {self.activity_log}"
        return log_str
