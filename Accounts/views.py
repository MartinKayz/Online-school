from django.shortcuts import render
from django.contrib.auth import get_user_model
from .forms import *

User = get_user_model()


def register(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
    return render(request, "Accounts/register.html", context)
