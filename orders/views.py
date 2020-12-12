from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from app_authentication.forms import UserUpdateForm, ProfileUpdateForm
from basket.models import ProductInBasket
from orders.forms import CheckoutForm


@login_required
def checkout_form(request):
    products = ProductInBasket.objects.all()
    count = ProductInBasket.objects.count()
    total_price = sum([ProductInBasket.get_total(items) for items in products])

    if request.method=='GET':
        form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        others = CheckoutForm(instance=request.user)

        context = {
            'form': form,
            'profile_form': profile_form,
            'products': products,
            'total_price': total_price,
            'count': count,
            'others': others,
        }
        return render(request, 'orders/checkout.html', context)
    else:
        form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.userprofile)
        others = CheckoutForm(request.POST or None)
        products = ProductInBasket.objects.all()

        if others.is_valid():
            others.save()
            products.delete()
            return redirect('thank-you')

        context = {
            'form': form,
            'profile_form': profile_form,
            'others': others,
        }
        return render(request, 'orders/checkout.html', context)


def thank_you_for_order(request):
    return render(request, 'orders/thank_you_page.html')
