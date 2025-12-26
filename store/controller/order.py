import random
from django.http.response import JsonResponse
from django.shortcuts import redirect,render
from django.contrib import  messages
from django.http.response import JsonResponse
from store.models import Product,Cart,Profile,Order,OrderItem
from django.contrib.auth.models import User

def order_view(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders':orders}
    return render(request,"store/order.html",context)

def view_order(request,t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context = {"order":order,"orderitems":orderitems}
    return render(request,"store/orderitem.html",context)