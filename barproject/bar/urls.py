from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('branch/<int:branch_id>/', views.branch, name='branch'),
    path('branch/1/employees', views.branch_employees, name='branch_employees'),

    #path('mark_order_complete/<int:order_id>/', views.mark_order_complete, name='mark_order_complete'),
]