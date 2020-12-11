from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from app.models import Product
from basket.forms import ProductForm, DeleteProductForm
from basket.models import ProductInBasket


@login_required
def cart_detail(request):
    products = ProductInBasket.objects.all()
    total_price = sum([ProductInBasket.get_total(items) for items in products])

    context = {
        'products': products,
        'total_price': total_price,
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
                'form': form,
            }
            return render(request, 'cart/review-product.html', context)


@login_required
def delete_product(request, pk):
    product_basket = ProductInBasket.objects.get(pk=pk)
    if request.method=="GET":
        form = DeleteProductForm(instance=product_basket)
        context = {
            'form': form
        }
        return render(request, 'cart/delete-product.html', context)
    else:
        product_basket.delete()
        return redirect('cart_detail')



