from django.contrib import admin
from django.urls import path
from users.views import login_user, profile_view, registration


app_name = 'users'

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('registration/', registration, name='registration'),
    path('profile/', profile_view, name='profile'),
]