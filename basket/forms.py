from django import forms

from basket.models import AddProduct


class ProductForm(forms.ModelForm):
    class Meta:
        model = AddProduct
        fields = ['name', 'quantity', 'price']
