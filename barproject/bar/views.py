from django.shortcuts import render
import calendar
from datetime import datetime
#from .models import Locations

def home(request):
    now = datetime.now()
    current_year = now.year
    current_month = now.strftime('%B')

    return render(request, 'home.html', {'current_year': current_year, 'current_month': current_month})

#def locations(request):
#    locations = Locations.objects.all()
#    return render(request, 'locations.html'), {'locations': locations}