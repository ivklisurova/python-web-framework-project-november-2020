from django.urls import path

from app_authentication import views


urlpatterns = [
    path('login/', views.login_user, name='login-user'),
    path('login-page/', views.login_page, name='login-page'),
    path('logout/', views.logout_user, name='logout-user'),
    path('register/', views.register, name='register-user'),
]
