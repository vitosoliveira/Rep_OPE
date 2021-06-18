from django.shortcuts import render, redirect
from app.models import Produto
from .models import Cart
from orders.models import Order
from django.contrib import messages



def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    produtos = cart_obj.products.all()
    return render(request, "carts/cart_home.html", {"cart": cart_obj, "produtos": produtos})

def cart_update(request):
    print(request.POST)
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:                                            
            product_obj = Produto.objects.get(id=product_id)
        except Produto.DoesNotExist:
            print("Mostrar mensagem ao usuário, esse produto acabou!")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request) 
        limitador = {
            "Massa": 1,
            "Recheio": 2,
            "Tamanho": 1,
            "Topping": 1   
        }

        tipo_produto = cart_obj.products.filter(tipo = product_obj.tipo)
        if len(tipo_produto) < limitador[product_obj.tipo]:
            cart_obj.products.add(product_obj)
        else:
            messages.info(request, 'Produo Já Adicionado no carrinho')
            return redirect("carts:home")

            
        
         
        # if product_obj in cart_obj.products.all(): 
        #     cart_obj.products.remove(product_obj) 
        # else: 
        request.session['cart_items'] = cart_obj.products.count()
    return redirect("cart:home")

def cart_delet(request):
    product_id = request.POST.get('product_id')
    product_obj = Produto.objects.get(id = product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request) 
    if product_obj in cart_obj.products.all(): 
        cart_obj.products.remove(product_obj)
    return redirect("cart:home") 
 
def checkout_home(request):
    #aqui a gente pega o carrinho
    cart_obj, cart_created= Cart.objects.new_or_get(request)
    order_obj = None
    #se o carrinho acabou de ser criado, ele tá zerado
    #ou se o carrinho já existir mas não tiver nada dentro
    produtos = cart_obj.products.all()
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:home")

    #aqui a order associada ao carrinho
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart = cart_obj, client_id = cart_obj.user_id)

    return render(request, "carts/checkout.html", {"object": order_obj, "produtos":produtos})