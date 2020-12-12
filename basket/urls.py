from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from basket import views

urlpatterns = [
                  path('cart-detail/', views.cart_detail, name='cart_detail'),
                  path('review-product/<int:pk>/', views.review_product, name='review-product'),
                  path('delete-product/<int:pk>/', views.delete_product, name='delete-product'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
