from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# from basket.models import AddProduct


class UserProfile(models.Model):
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'
