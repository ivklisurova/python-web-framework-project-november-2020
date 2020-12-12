from django.urls import path

from orders import views

urlpatterns = [
    path('checkout/', views.checkout_form, name='checkout'),
    path('thank-you/', views.thank_you_for_order, name='thank-you')

]
