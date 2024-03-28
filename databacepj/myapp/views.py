from django.shortcuts import render
from myapp.models import Locations
from myapp.models import Employee_Position
from myapp.models import Employees
from myapp.models import Branches
from myapp.models import Employee_Schedules
from myapp.models import Bar_Inventory
from myapp.models import Security_Logs
from myapp.models import BarTables
from myapp.models import Guesses
from myapp.models import Membership
from myapp.models import Feedback_Reviews
from myapp.models import Reservations

Locations = Locations.objects.all()
Employee_Position = Employee_Position.objects.all()
Employees = Employees.objects.all()
Branches = Branches.objects.all()
Employee_Schedules = Employee_Schedules.objects.all()
Bar_Inventory = Bar_Inventory.objects.all()
Security_Logs = Security_Logs.objects.all()
Guesses = Guesses.objects.all()
Membership = Membership.objects.all()
Feedback_Reviews = Feedback_Reviews.objects.all()
Reservations = Reservations.objects.all()

# Create your views here.

#def home(request):
#    return render(request, 'home.html', {'Locations': Locations, 'Employee_Position': Employee_Position, 'Employees': Employees, 'Branches': Branches, 'Employee_Schedules': Employee_Schedules, 'Bar_Inventory': Bar_Inventory, 'Security_Logs': Security_Logs, 'BarTables': BarTables, 'Guesses': Guesses, 'Membership': Membership, 'Feedback_Reviews': Feedback_Reviews, 'Reservations': Reservations})
def bartables(request):
    BarTables = BarTables.objects.all()
    return render(request, 'bartables.html', {'BarTables': BarTables})