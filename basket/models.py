from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from app.models import Product


class ProductInBasket(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    quantity = models.IntegerField(default=1)

    def get_total(self):
        total = self.price * self.quantity
        return int(total)



