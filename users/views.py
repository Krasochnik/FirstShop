from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def login_user(request):
    return render(request, "users/login_user.html")


def registration(request):
    return render(request, "users/registration.html")

@login_required
def profile_view(request):
    return render(request, "users/profile.html")

@login_required
def user_logout(request):
    logout(request)
    return render(request, "users/logout.html", {})