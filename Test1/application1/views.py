from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def about(request):
    vars = {
        "title": "Acerca de"
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

