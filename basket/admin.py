from django.contrib import admin


# Register your models here.
from basket.models import ProductInBasket

admin.site.register(ProductInBasket)