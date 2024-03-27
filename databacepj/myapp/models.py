from django.db import models

# Create your models here.
class Locations(models.Model):
    location_ID = models.AutoField(primary_key=True)
    address_no = models.CharField(max_length=40)
    street_name = models.CharField(max_length=30)
    city_name = models.CharField(max_length=30)
    province_name = models.CharField(max_length=25, blank=True, null=True)
    postal_code = models.CharField(max_length=12, blank=True, null=True)
    country_name = models.CharField(max_length=25)

class EPosition(models.Model):
    position_ID = models.CharField(primary_key=True, max_length=10)
    position_name = models.CharField(max_length=30)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()

class Employees(models.Model):
    employee_ID = models.CharField(primary_key=True, max_length=10)
    position_ID = models.ForeignKey(EPosition, on_delete=models.CASCADE)
    branch_ID = models.ForeignKey('Branches', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_info = models.DecimalField(max_digits=12, decimal_places=0)
    email = models.CharField(max_length=45)
    salary = models.IntegerField()
    hire_date = models.DateField()

class Branches(models.Model):
    branch_ID = models.AutoField(primary_key=True)
    location_ID = models.ForeignKey(Locations, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=40)
    employee_ID = models.ForeignKey(Employees, on_delete=models.CASCADE)

class Employee_Schedules(models.Model):
    schedule_ID = models.AutoField(primary_key=True)
    branch_ID = models.ForeignKey(Branches, on_delete=models.CASCADE)
    employee_ID = models.ForeignKey(Employees, on_delete=models.CASCADE)
    shift_start = models.TimeField()
    shift_end = models.TimeField()

class Bar_Inventory(models.Model):
    product_ID = models.AutoField(primary_key=True)
    branch_ID = models.ForeignKey(Branches, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.IntegerField()

class Security_Logs(models.Model):
    log_ID = models.AutoField(primary_key=True)
    branch_ID = models.ForeignKey(Branches, on_delete=models.CASCADE)
    employee_ID = models.ForeignKey(Employees, on_delete=models.CASCADE)
    log_time = models.TimeField()
    activity_log = models.BooleanField()

class BarTables(models.Model):
    table_ID = models.AutoField(primary_key=True)
    start_time = models.TimeField()
    table_status = models.BooleanField()

class Guesses(models.Model):
    branch_ID = models.ForeignKey(Branches, on_delete=models.CASCADE)
    table_ID = models.ForeignKey(BarTables, on_delete=models.CASCADE)
    guess_first_name = models.CharField(max_length=30)
    guess_last_name = models.CharField(max_length=30)
    guess_band = models.CharField(max_length=30)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['branch_ID', 'table_ID'], name='unique_guess')
        ]

class Membership(models.Model):
    membership_id = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    contact_info = models.DecimalField(max_digits=12, decimal_places=0)
    membership_status = models.BooleanField()

class Feedback_Reviews(models.Model):
    review_ID = models.AutoField(primary_key=True)
    membership_id = models.ForeignKey(Membership, on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedbacks = models.TextField()

class Reservations(models.Model):
    reservation_ID = models.AutoField(primary_key=True)
    branch_ID = models.ForeignKey(Branches, on_delete=models.CASCADE)
    table_ID = models.ForeignKey(BarTables, on_delete=models.CASCADE)
    membership_id = models.ForeignKey(Membership, on_delete=models.CASCADE)
    reservation_time = models.TimeField()
    number_of_guests = models.IntegerField()