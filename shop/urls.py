from django.contrib import admin
from django.urls import path
from shop.views import home, profile_view, login_user
from django.contrib.auth.views import LoginView

app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('profile', profile_view, name='profile'),
    path('login', login_user, name='login'),



]