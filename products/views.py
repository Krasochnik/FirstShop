from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from products.models import Product, Category


# Create your views here.
def products(request):
    products_list=Product.objects.all()
    category=Category.objects.all()
    
    context={"products": products_list,
             "category":category
             
             }
    return render(request, "products/products.html", context )

def product_detail(request):
    return render(request, "products/product_detail.html")

# Create your views here.
