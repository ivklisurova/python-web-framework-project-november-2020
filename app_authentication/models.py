from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserProfile(models.Model):
    address = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
