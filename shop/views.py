from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "shop/home.html")

def about(request):
    return render(request, "shop/about.html")

def login_user(request):
    return render(request, "registration/login.html")


@login_required
def profile_view(request):
    return render(request, "shop/profile.html")


@login_required
def user_logout(request):
    logout(request)
    return render(request, "registration/logout.html", {})
