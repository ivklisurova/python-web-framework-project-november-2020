from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from app.models import Team, Product


# Main page
def index(req):
    team = Team.objects.all()
    context = {
        'team': team
    }
    return render(req, 'index.html', context)


# Contact page
def contact_us(req):
    return render(req, 'contact_us.html')


# Product page
def all_products(req):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(req, 'all_products.html', context)


