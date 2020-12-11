from django.db import models


# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='team_images')
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=20, default='cake')
    picture = models.ImageField(upload_to='product_images')
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    description = models.TextField()


    def __str__(self):
        return f'{self.name}'
