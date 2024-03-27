# Register your models here.
from django.contrib import admin
from .models import Locations, Employee_Position, Employees, Branches, Employee_Schedules, Bar_Inventory, Security_Logs, BarTables, Guesses, Membership, Feedback_Reviews, Reservations

admin.site.register(Locations)
admin.site.register(Employee_Position)
admin.site.register(Employees)
admin.site.register(Branches)
admin.site.register(Employee_Schedules)
admin.site.register(Bar_Inventory)
admin.site.register(Security_Logs)
admin.site.register(BarTables)
admin.site.register(Guesses)
admin.site.register(Membership)
admin.site.register(Feedback_Reviews)
admin.site.register(Reservations)
