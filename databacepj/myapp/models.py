from django.db import models

class Locations(models.Model):
    location_ID = models.AutoField(primary_key=True)
    address_no = models.CharField(max_length=40)
    street_name = models.CharField(max_length=30)
    city_name = models.CharField(max_length=30)
    province_name = models.CharField(max_length=25, blank=True, null=True)
    postal_code = models.CharField(max_length=12, blank=True, null=True)
    country_name = models.CharField(max_length=25)

class Employee_Position(models.Model):
    position_ID = models.CharField(primary_key=True, max_length=10)
    position_name = models.CharField(max_length=30)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()

class Employees(models.Model):
    employee_ID = models.CharField(primary_key=True, max_length=10)
    position_ID = models.ForeignKey(Employee_Position, on_delete=models.CASCADE)
    branch = models.ForeignKey('Branches', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_info = models.DecimalField(max_digits=12, decimal_places=0)
    email = models.CharField(max_length=45)
    salary = models.IntegerField()
    hire_date = models.DateField()

class Branches(models.Model):
    branch_ID = models.AutoField(primary_key=True)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=40)
    employee_ID = models.CharField(max_length=10) 

class Employee_Schedules(models.Model):
    schedule_ID = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    employee_ID = models.CharField(max_length=10)
    shift_start = models.TimeField()
    shift_end = models.TimeField()

class Bar_Inventory(models.Model):
    product_ID = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.IntegerField()

class Security_Logs(models.Model):
    log_ID = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    employee_ID = models.CharField(max_length=10)
    log_time = models.TimeField()
    activity_log = models.BooleanField()

class BarTables(models.Model):
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    table_ID = models.CharField(primary_key=True, max_length=8)
    start_time = models.TimeField()
    check_out_time = models.TimeField()
    table_status = models.BooleanField()

    class Meta:
        db_table = 'BarTables'

class Guesses(models.Model):
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    table_ID = models.CharField(max_length=8)
    guess_first_name = models.CharField(max_length=30)
    guess_last_name = models.CharField(max_length=30)
    guess_band = models.CharField(max_length=30)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['branch', 'table_ID'], name='unique_guess')
        ]

class Membership(models.Model):
    membership_id = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    contact_info = models.DecimalField(max_digits=12, decimal_places=0)
    membership_status = models.BooleanField()

class Feedback_Reviews(models.Model):
    review_ID = models.AutoField(primary_key=True)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    rating = models.IntegerField()
    feedbacks = models.TextField()

class Reservations(models.Model):
    reservation_ID = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    table = models.ForeignKey(BarTables, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    reservation_time = models.TimeField()
    number_of_guests = models.IntegerField()
