from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def products(request):
    return render(request, "products/products.html" )

def product_detail(request):
    return render(request, "products/product_detail.html")

# Create your views here.
