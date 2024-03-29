from django import forms
from django.forms import formset_factory
from .models import Orders, OrderProduct, BarInventory, Bartables

class ProductNameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.product_name

class OrderItemForm(forms.Form):
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 6)]

    def __init__(self, *args, **kwargs):
        branch_id = kwargs.pop('branch_id')
        super(OrderItemForm, self).__init__(*args, **kwargs)
        self.fields['product'].queryset = BarInventory.objects.filter(branch_id=branch_id)

    product = ProductNameChoiceField(queryset=BarInventory.objects.none())
    quantity = forms.ChoiceField(choices=QUANTITY_CHOICES)

OrderItemFormSet = formset_factory(OrderItemForm, extra=1)

class TableIDChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.table_id

class OrderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        branch_id = kwargs.pop('branch_id', None)
        super(OrderForm, self).__init__(*args, **kwargs)
        if branch_id:
            self.fields['table_id'].queryset = Bartables.objects.filter(branch_id=branch_id)

    table_id = TableIDChoiceField(queryset=Bartables.objects.none())