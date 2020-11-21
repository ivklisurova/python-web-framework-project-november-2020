from django.shortcuts import render


# Create your views here.

def index(req):
    return render(req, 'index.html')


def contact_us(req):
    return render(req, 'contact_us.html')


def all_products(req):
    return render(req, 'all_products.html')
