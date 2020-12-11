from django.db import models

# Create your models here.
from app_authentication.models import UserProfile


class Order(models.Model):
    username = models.CharField(max_length=40)
    phone = models.IntegerField()
    status = models.CharField(max_length=10,default='processed', editable=False)

