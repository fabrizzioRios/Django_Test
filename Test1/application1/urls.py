from django.contrib import admin

from django.urls import path
from application1.views import about, home, contact, signup
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home/', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('', LoginView.as_view(template_name="base.html"), name="login"),
    path('cerrar/', LogoutView.as_view(), name="logout"),
    path('signup/', signup, name="signup"),
]