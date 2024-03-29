from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
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


def home(request):
    now = datetime.now()
    current_year = now.year
    current_month = now.strftime('%B')
    reviews = FeedbackReviews.objects.all()

    return render(request, 'home.html', {'current_year': current_year, 'current_month': current_month, 'reviews': reviews})

def branch(request, branch_id):
    return render(request, 'branch.html')

def branch_employees(request):
    return render(request, 'branch_employees.html')



def customer_menu(request):
    return render(request, 'customer_menu.html')

@require_POST
def mark_order_complete(request, order_id):
    order = get_object_or_404(OrderItems, id=order_id)
    order.order_completed = True
    order.save()
    return redirect('order_view')