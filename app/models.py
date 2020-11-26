from django.db import models


# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='team_images')
    description = models.TextField()
