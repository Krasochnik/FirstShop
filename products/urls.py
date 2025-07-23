from django.urls import path
from products.views import products, product_detail

app_name = 'products'

urlpatterns = [
    path('search/', products, name='search'),
    path('<slug:category_slug>/', products, name='products'),
    path('detail/<slug:product_slug>', product_detail, name='product_detail'),
]
