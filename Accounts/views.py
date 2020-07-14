from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

User = get_user_model()


def register(request):
    if request.user.is_authenticated:
        return redirect("mainsite:index")
    else:
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('mainsite:index')
        context = {
            'form': form,
        }

    return render(request, "Accounts/register.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("mainsite:index")
    else:

        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.error(
                    request, "Sorry we couldn't Login you in, Check your Username and Password")
                return redirect('mainsite:index')
            else:
                messages.info(request, "Username Or Password is Inncorrect ")

        context = {
            'form': form
        }
    return render(request, 'Accounts/loginpage.html', context)


def logoutUser(request):
    logout(request)
    return redirect("mainsite:index")
