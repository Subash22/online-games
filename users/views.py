from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import get_user_model

User = get_user_model()


def user_register(request):
    if request.method == "POST":
        r_form = UserRegisterForm(request.POST)
        if r_form.is_valid():
            r_form.save()
            messages.success(request, f'User created succesfully.')
            return redirect('/')
        else:
            messages.error(request, f'Error while creating account.')
            return redirect('/register')

    r_form = UserRegisterForm()
    context = {
        'title': 'Register',
        'r_form': r_form
    }
    return render(request, 'users/register.html', context)
