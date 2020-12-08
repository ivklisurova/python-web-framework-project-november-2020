from django.contrib import admin


# Register your models here.

class AddProductAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'price')
