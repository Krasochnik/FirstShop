from django.shortcuts import render
from products.models import Category


# Create your views here.
def home(request):
    context={"title":"Home page" }
    return render(request, "shop/home.html", context)

def about(request):
    context={"title":"about" }
    return render(request, "shop/about.html",context)


