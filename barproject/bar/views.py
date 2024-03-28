from django.shortcuts import render
from .models import Locations

# Create your views here.
def locations(request):
    locations = Locations.objects.all()
    return render(request, 'locations.html'), {'locations': locations}