from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.forms import formset_factory
from .forms import OrderForm, OrderItemFormSet
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

    return render(request, 'home.html', {'current_year': current_year, 'current_month': current_month, 'reviews': reviews})

def branch(request, branch_id):
    return render(request, 'branch.html', {'branch_id': branch_id})

def branch_employees(request, branch_id):
    return render(request, 'branch_employees.html', {'branch_id': branch_id})

def customer_menu(request, branch_id):
    inventory = BarInventory.objects.filter(branch_id=branch_id)
    tables = Bartables.objects.filter(branch_id=branch_id)
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

def table_orders(request, branch_id, table_id):
    orders = Orders.objects.filter(branch_id=branch_id, table_id=table_id).prefetch_related('orderproduct_set')
    total_bill = sum(order_product.total_price() for order in orders for order_product in order.orderproduct_set.all())
    return render(request, 'table_orders.html', {'orders': orders, 'table_id': table_id, 'total_bill': total_bill})

