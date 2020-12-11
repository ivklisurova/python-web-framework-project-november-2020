from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect

# Create your views here.

# Login/Logout/Register
from app_authentication.forms import RegisterForm, ProfileForm, LoginForm, UserUpdateForm, \
    ProfileUpdateForm, UserDeleteForm
from orders.models import Order


@transaction.atomic
def register(req):
    if req.method=='GET':

        context = {
            'form': RegisterForm(),
            'profile': ProfileForm(),
        }

        return render(req, 'auth/register.html', context)

    else:
        form = RegisterForm(req.POST)
        profile = ProfileForm(req.POST, req.FILES)

        if form.is_valid() and profile.is_valid():
            user = form.save()
            user_profile = profile.save(commit=False)
            user_profile.user = user
            user_profile.save()

            login(req, user)
            return redirect('index')

        context = {
            'form': form,
            'profile': profile,
        }
        return render(req, 'auth/register.html', context)


def login_user(req):
    if req.method=='GET':
        context = {
            'login_form': LoginForm()
        }
        return render(req, 'auth/login.html', context)
    else:
        login_form = LoginForm(req.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(req, username=username, password=password)

            if user:
                if user.is_active:
                    login(req, user)
                    return redirect('index')
            else:
                messages.error(req, 'username or password not correct')
                return redirect('login-user')


def logout_user(req):
    logout(req)
    return redirect('index')


def user_profile(req):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(req, 'auth/profile.html', context)


@login_required
def update_profile(req):
    if req.method=='GET':
        form = UserUpdateForm(instance=req.user)
        profile_form = ProfileUpdateForm(instance=req.user.userprofile)

        context = {
            'form': form,
            'profile_form': profile_form,
        }
        return render(req, 'auth/edit-profile.html', context)
    else:
        form = UserUpdateForm(req.POST, instance=req.user)
        profile = ProfileUpdateForm(req.POST, req.FILES, instance=req.user.userprofile)

        if form.is_valid() and profile.is_valid():
            form.save()
            profile.save()
            return redirect('user-profile')

        context = {
            'form': form,
            'profile': profile,
        }
        return render(req, 'auth/edit-profile.html', context)


@login_required
def delete_profile(req):
    if req.method=='GET':
        delete_form = UserDeleteForm(instance=req.user)

        context = {
            'delete_form': delete_form,
        }

        return render(req, 'auth/delete-profile.html', context)
    else:
        UserDeleteForm(req.POST, instance=req.user)
        user = req.user
        user.delete()
        return redirect('index')
