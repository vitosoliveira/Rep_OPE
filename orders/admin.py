
from django.contrib import admin

from .models import Order



class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['pedido','client', 'produtos', 'telefone', 'data_pedido']

    def produtos(self, obj):
        return ", \n".join([p.nome for p in obj.cart.products.all()])
    
    def telefone(self, obj):
        return obj.client.telefone

    def data_pedido(self,obj):
        return obj.data_compra
    
    def pedido(self,obj):
        return obj.order_id

admin.site.register(Order, OrderAdmin)
