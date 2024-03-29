from django import forms
from .models import Orders, OrderProduct, BarInventory, Bartables
from django.shortcuts import render, redirect

class OrderItemForm(forms.Form):
    product = forms.ModelChoiceField(queryset=BarInventory.objects.all())
    quantity = forms.IntegerField(min_value=1, max_value=5)

class OrderForm(forms.Form):
    table_id = forms.ModelChoiceField(queryset=Bartables.objects.all())
    order_items = forms.FormSetField(OrderItemForm)

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Orders.objects.create(table_id=form.cleaned_data['table_id'])
            for item_form in form.cleaned_data['order_items']:
                OrderProduct.objects.create(
                    order=order,
                    item=item_form.cleaned_data['product'],
                    quantity=item_form.cleaned_data['quantity'],
                    branch=item_form.cleaned_data['product'].branch
                )
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})