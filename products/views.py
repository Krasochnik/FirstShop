from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from products.models import Product
from products.utils import q_search


# Create your views here.
def products(request, category_slug=None):
   
    page = request.GET.get('page', 1)
    currency = request.GET.get('currency', None)
    on_sale = request.GET.get('on_sale', None)
    query = request.GET.get('q', None)

    if category_slug=='all':
        products_list=Product.objects.all()
    elif query:
        products_list = q_search(query)
    else:
        products_list= get_list_or_404(Product.objects.filter(category__slug=category_slug))
       

    if on_sale:
        products_list=Product.objects.filter(discount__gt=0)

    if currency and currency != "default":
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
             }
    return render(request, "products/product_detail.html", context)


