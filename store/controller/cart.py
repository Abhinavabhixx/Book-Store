from django.shortcuts import redirect, render
from django.http import JsonResponse
from store.models import Product, Cart

def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.filter(id=prod_id).first()

            if product_check:
                if Cart.objects.filter(user=request.user, product_id=prod_id).exists():
                    return JsonResponse({'status': 'Product already in cart'})
                else:
                    prod_qty = int(request.POST.get('product_quantity'))

                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(
                            user=request.user,
                            product_id=prod_id,
                            product_quantity=prod_qty
                        )
                        return JsonResponse({'status': 'Product added in cart'})
                    else:
                        return JsonResponse({'status': 'Only ' + str(product_check.quantity) + " quantity available"})
            else:
                return JsonResponse({'status': 'No such product'})
        else:
            return JsonResponse({'status': 'Login to continue'})
    return redirect('/')

def viewcart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        context = {'cart': cart}
        return render(request, 'store/cart.html', context)
    else:
        return redirect('/loginpage')


def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if Cart.objects.filter(user=request.user, product_id=prod_id):
            prod_qty = int(request.POST.get('product_quantity'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
        return JsonResponse({'status': 'Product updated in cart'})
    return redirect('/')

def deletecartitem(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('product_id'))
        if (Cart.objects.filter(user=request.user, product_id=prod_id)):
            cartitem = Cart.objects.get(product_id=prod_id,user=request.user)
            cartitem.delete()
            return  JsonResponse({'status':'Delete successfully'})
    return redirect('/')


