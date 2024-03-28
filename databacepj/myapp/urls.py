from django.urls import path
from . import views

urlpatterns = [
    path('bartable/', views.bartables, name='bartables'),
]
