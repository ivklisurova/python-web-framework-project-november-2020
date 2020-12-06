from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.

class AddProduct(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    quantity = models.IntegerField(default=1)
