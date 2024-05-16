from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from products.models import Category


# Create your views here.
def home(request):
    category=Category.objects.all()
    context={"category":category }
    return render(request, "shop/home.html", context)

def about(request):
    category=Category.objects.all()
    context={"category":category }
    return render(request, "shop/about.html",context)

def login_user(request):
    return render(request, "registration/login.html")


@login_required
def profile_view(request):
    return render(request, "shop/profile.html")


@login_required
def user_logout(request):
    logout(request)
    return render(request, "registration/logout.html", {})
