from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('branch/<int:branch_id>/', views.branch, name='branch'),
    path('branch/<int:branch_id>/employees', views.branch_employees, name='branch_employees'),
    path('branch/<int:branch_id>/customers', views.customer_menu, name='customer_menu'),
    path('branch/<int:branch_id>/customers/<str:table_id>/order_success/', views.order_success, name='order_success'),
    path('branch/<int:branch_id>/table_orders/<str:table_id>/', views.table_orders, name='table_orders'),

    #path('mark_order_complete/<int:order_id>/', views.mark_order_complete, name='mark_order_complete'),
]