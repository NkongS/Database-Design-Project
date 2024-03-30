from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.forms import formset_factory
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.http import JsonResponse
from .forms import OrderForm, OrderItemFormSet, ReservationForm, ReviewForm
from django.core import serializers
from datetime import datetime
from .models import BarInventory
from .models import Locations
from .models import Bartables
from .models import Branches
from .models import EmployeePosition
from .models import Employees
from .models import FeedbackReviews
from .models import Guesses
from .models import Membership
from .models import Reservations
from .models import SecurityLogs
from .models import Orders
from .models import OrderProduct


def home(request):
    now = datetime.now()
    current_year = now.year
    current_month = now.strftime('%B')
    reviews = FeedbackReviews.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = FeedbackReviews(
                membership=form.cleaned_data['membership'],
                rating=form.cleaned_data['rating'],
                feedbacks=form.cleaned_data['feedbacks']
            )
            review.save()
            return redirect('home')
    else:
        form = ReviewForm()

    return render(request, 'home.html', {'current_year': current_year, 'current_month': current_month, 'reviews': reviews, 'form': form})

def branch(request, branch_id):
    return render(request, 'branch.html', {'branch_id': branch_id})

def branch_employees(request, branch_id):
    return render(request, 'branch_employees.html', {'branch_id': branch_id})

def customer_menu(request, branch_id):
    inventory = BarInventory.objects.filter(branch_id=branch_id)
    tables = Bartables.objects.filter(branch_id=branch_id).order_by('table_id')
    if request.method == 'POST':
        form = OrderForm(request.POST, branch_id=branch_id)
        formset = OrderItemFormSet(request.POST, form_kwargs={'branch_id': branch_id})
        if form.is_valid() and formset.is_valid():
            table = form.cleaned_data['table_id']
            first_item_form = formset[0]
            branch = first_item_form.cleaned_data['product'].branch
            item = first_item_form.cleaned_data['product']
            order = Orders.objects.create(table_id=table, branch=branch, item=item)
            for item_form in formset:
                OrderProduct.objects.create(
                    order=order,
                    item=item_form.cleaned_data['product'],
                    quantity=item_form.cleaned_data['quantity'],
                    branch=item_form.cleaned_data['product'].branch
                )
            return redirect('order_success', branch_id=branch_id, table_id=table.table_id)
    else:
        form = OrderForm(branch_id=branch_id)
        formset = OrderItemFormSet(form_kwargs={'branch_id': branch_id})
    return render(request, 'customer_menu.html', {'form': form, 'formset': formset, 'inventory': inventory, 'tables': tables})

def order_success(request, branch_id, table_id):
    return render(request, 'order_success.html', {'branch_id': branch_id})

def table_orders(request, branch_id, table_id, from_employees=False):
    orders = Orders.objects.filter(branch_id=branch_id, table_id=table_id).prefetch_related('orderproduct_set')
    total_bill = sum(order_product.total_price() for order in orders for order_product in order.orderproduct_set.all())
    return render(request, 'table_orders.html', {'orders': orders, 'table_id': table_id, 'total_bill': total_bill, 'from_employees': from_employees})

def view_orders(request, branch_id):
    tables = Bartables.objects.filter(branch_id=branch_id).order_by('table_id')
    return render(request, 'orders.html', {'tables': tables})

@csrf_exempt
def checkout(request):
    if request.method == 'POST':
        table_id = request.POST.get('table_id', None)
        if table_id is not None:
            Orders.objects.filter(table_id=table_id).delete()
            return redirect(request.META['HTTP_REFERER'])
    return JsonResponse({'success': False})

def management(request, branch_id):
    branches = Branches.objects.filter(branch_id=branch_id)
    employees = Employees.objects.filter(branch=branch_id)
    guests = Guesses.objects.filter(branch=branch_id)
    memberships = Membership.objects.all()
    security_logs = SecurityLogs.objects.filter(branch=branch_id)

    context = {
        'branches': branches,
        'employees': employees,
        'guests': guests,
        'memberships': memberships,
        'security_logs': security_logs,
    }

    return render(request, 'management.html', context)

@csrf_exempt
def mark_complete(request, order_id):
    if request.method == 'POST':
        completed = request.POST.get('completed', 'off')
        if completed == 'on':
            order = Orders.objects.get(pk=order_id)
            order.completed = True
            order.save()
        return redirect(request.META['HTTP_REFERER'])
    
def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            branch = form.cleaned_data['branch']
            table = form.cleaned_data['table']
            membership = form.cleaned_data['membership']
            number_of_guests = form.cleaned_data['number_of_guests']
            reservation_time = form.cleaned_data['reservation_time']

            if table:
                reservation = Reservations.objects.create(
                    branch=branch,
                    table=table,
                    membership=membership,
                    reservation_time=reservation_time,
                    number_of_guests=number_of_guests
                )

                table.table_status = True
                table.start_time = reservation_time
                table.save()

                return redirect('reserve_success', branch_id=branch.id, table_id=table.id)
    else:
        form = ReservationForm()

    return render(request, 'reservation.html', {'form': form})

def load_tables(request):
    branch_id = request.GET.get('branch')
    tables = Bartables.objects.filter(branch_id=branch_id, table_status=False).order_by('table_id')
    return render(request, 'tables_dropdown_list_options.html', {'tables': tables})

