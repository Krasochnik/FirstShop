from django.contrib import admin
from django.urls import path
from products.views import products, product_detail
from django.contrib.auth.views import LoginView

app_name = 'products'

urlpatterns = [
    path('<slug:category_slug>/', products, name='products'),
    path('detail/<slug:product_slug>', product_detail, name='product_detail'),
]