from django.shortcuts import render

# Create your views here.
from app.models import Team


def index(req):
    team = Team.objects.all()
    context = {
        'team': team
    }
    return render(req, 'index.html', context)


def contact_us(req):
    return render(req, 'contact_us.html')


def all_products(req):
    return render(req, 'all_products.html')


def login(req):
    return render(req, 'login.html')
