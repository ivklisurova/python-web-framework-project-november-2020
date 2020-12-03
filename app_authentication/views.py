from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.shortcuts import render, redirect

# Create your views here.

# Login/Logout/Register
from app_authentication.forms import RegisterForm, ProfileForm, LoginForm


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
