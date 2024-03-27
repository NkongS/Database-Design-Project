from django.db import models

# Create your models here.
class Branch(models.Model):
    branch_ID = models.AutoField(primary_key=True)
    location_ID = models.IntegerField()
    branch_name = models.CharField(max_length=40)
    manager_ID = models.CharField(max_length=10)

    class Meta:
        db_table = 'Branches'