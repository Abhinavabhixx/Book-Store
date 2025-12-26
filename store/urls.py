from django.urls import path
from.import views
from store.controller import authview,cart,wishlist,checkout,order


urlpatterns = [
    path('',views.home,name='home'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:slug>',views.collectionsview,name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>/', views.productview, name='productview'),

    path('register/',authview.register,name='register'),
    path('login/',authview.loginpage,name='login'),
    path('logout/',authview.logoutpage,name='logout'),

    path('add-to-cart/', cart.addtocart, name='add-to-cart'),
    path('cart',cart.viewcart,name='cart'),
    path('update-cart',cart.updatecart,name='update-cart'),
    path('delete-cart-item',cart.deletecartitem,name='delete-cart-item'),

    path('wishlist',wishlist.index,name='wishlist'),
    path('add-to-wishlist', wishlist.addtowishlist, name='add-to-wishlist'),
    path('delete-wishlist-item', wishlist.deletewishlistitem, name='delete-wishlist-item'),

    path('checkout', checkout.index, name='checkout'),
    path('place-order',checkout.placeorder,name='placeorder'),
    path('proceed-to-pay',checkout.razorpaycheck,name='proceed-to-pay'),

    path('order/',order.order_view,name='order'),
    path('view-order/<str:t_no>/',order.view_order,name='orderview'),

]
