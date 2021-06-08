from django.shortcuts import render, redirect
from app.models import Produto
from .models import Cart


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/cart_home.html", {"cart": cart_obj})

def cart_update(request):
    print(request.POST)
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:                                                    #*******************************************************
            product_obj = Produto.objects.get(id=product_id)
        except Produto.DoesNotExist:
            print("Mostrar mensagem ao usuário, esse produto acabou!")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request) 
        cart_obj.products.add(product_obj)
        # if product_obj in cart_obj.products.all(): 
        #     cart_obj.products.remove(product_obj) 
        # else: 
    return redirect("cart:home")