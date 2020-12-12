from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from app.models import Product
from basket.forms import ProductForm, DeleteProductForm, UpdateProductForm
from basket.models import ProductInBasket


@login_required
def cart_detail(request):
    products = ProductInBasket.objects.all()
    total_price = sum([ProductInBasket.get_total(items) for items in products])
    count_products = len(products)
    is_empty = False

    if count_products == 0:
        is_empty = True


    context = {
        'products': products,
        'total_price': total_price,
        'is_empty': is_empty,
    }
    return render(request, 'cart/cart_detail.html', context)


@login_required
def review_product(request, pk):
    product_basket = Product.objects.get(pk=pk)

    if request.method=='GET':
        form = UpdateProductForm(instance=product_basket)

        context = {
            'form': form,
        }
        return render(request, 'cart/review-product.html', context)

    else:
        # qty = request.POST.get('quantity')
        form = ProductForm(request.POST or None)
        is_positive = True
        qty = int(form['quantity'].value())

        if qty < 1:
            is_positive = False

        if form.is_valid() and is_positive:
            form.save()
            return redirect('all_products')
        else:
            messages.error(request, 'please fill valid quantity')
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
