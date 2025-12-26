from django.shortcuts import render, redirect
from pyexpat.errors import messages
from unicodedata import category
from .models import *

# Create your views here.

def home(request):
    trending_products = Product.objects.filter(trending=1)
    context = {"trending_products": trending_products}
    return render(request, "store/home.html", context)

def collections(request):
    category = Category.objects.filter(status=0)
    context = {"category":category}
    return render(request,'store/collections.html',context)

def collectionsview(request,slug):
    if(Category.objects.filter(slug=slug,status=0)):
        products=Product.objects.filter(category__slug=slug)
        category=Category.objects.filter(slug=slug).first()
        context = {"products":products,"category":category}
        return render(request,'store/products/home.html',context)
    else:
        messages.warning(request,"category not found")
        return redirect('collections')

def productview(request,cate_slug,prod_slug):
    if Category.objects.filter(slug=cate_slug,status=0).exists():
        if Product.objects.filter(slug=prod_slug,status=0).exists():
            products=Product.objects.filter(slug=prod_slug,status=0).first()
            context = {"products":products}
        else:
            messages.error(request,"product not found!")
            return redirect('collections')
    else:
        messages.error(request,"no such category")
        return redirect('collections')
    return render(request,'store/products/view.html',context)
