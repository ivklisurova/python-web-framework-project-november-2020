from django import forms

from basket.models import AddProduct


class ProductForm(forms.ModelForm):
    class Meta:
        model = AddProduct
        fields = ['name', 'quantity', 'price']


class DeleteProductForm(ProductForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True
