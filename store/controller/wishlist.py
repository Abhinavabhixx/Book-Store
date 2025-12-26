from django.shortcuts import redirect,render
from django.contrib import  messages
from django.http.response import JsonResponse
from store.models import Product,Cart,Wishlist

def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context = {'wishlist':wishlist}
    return render(request,"store/wishlist.html",context)

def addtowishlist(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id = prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                    return  JsonResponse({"status":"Product already in wishlist"})
                else:
                    Wishlist.objects.create(user=request.user,product_id=prod_id)
                    return JsonResponse({'status':'Product added to wishlist'})
            else:
                return JsonResponse({'status':'No such product found'})
        else:
            return JsonResponse({'status':'Login to continue'})
    return redirect('/')

def deletewishlistitem(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            try:
                wishlist_item =Wishlist.objects.get(user=request.user,product_id =prod_id)
                wishlist_item.delete()
                return  JsonResponse({'status':'Product removed from wishlist'})
            except Wishlist.DoesNotExist:
                return JsonResponse({'status':'Product not found in wishlist'})
        else:
            return JsonResponse({'status':'Login to continue'})
    return redirect('/')
