from django.contrib import admin

# Register your models here.
from app_authentication.models import UserProfile

admin.site.register(UserProfile)
