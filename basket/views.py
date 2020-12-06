from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from app.models import Product
from basket.forms import ProductForm
from basket.models import AddProduct


@login_required
def cart_detail(request):
    products = AddProduct.objects.all()

    context = {
        'products': products
    }
    return render(request, 'cart/cart_detail.html', context)


@login_required
def review_product(request, pk):
    product_basket = Product.objects.get(pk=pk)

    if request.method=='GET':
        form = ProductForm(instance=product_basket)

        context = {
            'form': form,
        }
        return render(request, 'cart/review-product.html', context)

    else:
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('all_products')
        else:
            context = {
                'form': form
            }
            return render(request, 'cart/review-product.html', context)


def delete_product(request):
    pass