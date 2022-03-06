from django.contrib import admin
from django.urls import path
from application1.views import about, home, contact

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
]