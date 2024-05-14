from django.contrib import admin
from django.urls import path
from shop.views import home, profile_view, login_user, about
from django.contrib.auth.views import LoginView

app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('about', home, name='about'),
    path('profile', profile_view, name='profile'),
    path('login', login_user, name='login'),



]