from django.contrib import admin

# Register your models here.
from app.models import Team, Product

admin.site.register(Team)
admin.site.register(Product)
