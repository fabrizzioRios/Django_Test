from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def about(request):
    vars = {
        "title": "Informacion prueba"
    }
    return render(request, "about.html", context=vars)


def home(request):
    vars = {
        "title": "Inicio"
    }
    return render(request, "home.html", context=vars)


def contact(request):
    vars = {
        "title": "Contact"
    }
    return render(request, "contact.html", context=vars)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
