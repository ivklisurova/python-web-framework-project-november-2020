from django import forms
from django.contrib.auth.models import User

from basket.models import ProductInBasket


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductInBasket
        fields = ['name', 'quantity', 'price']


class UpdateProductForm(ProductForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (name, field) in self.fields.items():
            if name == 'name' or name == 'price':
                field.widget.attrs['readonly'] = True


class DeleteProductForm(ProductForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True
