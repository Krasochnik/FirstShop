from django.contrib import admin
from django.urls import path
from shop.views import home, profile_view, user_logout

urlpatterns = [
    path('', home, name='home'),
    path('profile', profile_view, name='profile'),
    path('logout', user_logout, name='logout'),



]