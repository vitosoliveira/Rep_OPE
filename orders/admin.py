
from django.contrib import admin

from .models import Order



class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['client', 'produtos', 'telefone']

    def produtos(self, obj):
        return ", \n".join([p.nome for p in obj.cart.products.all()])
    
    def telefone(self, obj):
        return obj.client.telefone

admin.site.register(Order, OrderAdmin)
