from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from products.models import Product, Category


# Create your views here.
def products(request, category_slug=None):
   
    page = request.GET.get('page', 1)
    currency = request.GET.get('currency', None)
    on_sale = request.GET.get('on_sale', None)

    if category_slug=='all':
        products_list=Product.objects.all()
    else:
        products_list=Product.objects.filter(category__slug=category_slug)

    if on_sale:
        products_list=Product.objects.filter(discount__gt=0)

    if currency:
        products_list=Product.objects.order_by(currency)


    paginator = Paginator(products_list, 3)
    current_page = paginator.page(int(page))

    context={
        "title": "Каталог",
        "products": current_page,
        "slug_url": category_slug,

             }
    return render(request, "products/products.html", context )

def product_detail(request, product_slug=None):
    product=Product.objects.get(slug=product_slug)
    context={
        "products": product,
        "slug_url": product_slug,
             }
    return render(request, "products/product_detail.html", context)

# Create your views here.
