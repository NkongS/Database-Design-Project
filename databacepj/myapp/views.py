from django.shortcuts import render
from myapp.models import Branch

branches = Branch.objects.all()

# Create your views here.
