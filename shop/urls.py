from django.contrib import admin
from django.urls import path
from shop.views import home, about

app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),





]
