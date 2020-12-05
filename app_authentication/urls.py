from django.urls import path

from app_authentication import views


urlpatterns = [
    path('login/', views.login_user, name='login-user'),
    path('logout/', views.logout_user, name='logout-user'),
    path('register/', views.register, name='register-user'),
    path('profile/', views.user_profile, name='user-profile'),
    path('edit/', views.update_profile, name='user-update'),
    path('delete/', views.delete_profile, name='delete-profile'),
]
