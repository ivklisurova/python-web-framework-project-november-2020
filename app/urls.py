from django.urls import path

from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact_us, name='contact'),
    path('products/', views.all_products, name='all_products')
]
