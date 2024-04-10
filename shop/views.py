from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from shop.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()

    return render(request, 'shop/home.html', {'product': products} )

@login_required
def profile_view(request):
    return render(request, 'shop/profile.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html', {})