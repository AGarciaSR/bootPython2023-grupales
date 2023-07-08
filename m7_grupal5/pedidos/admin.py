from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from pedidos.models import Producto, Pedido, ProductoComprado

class ProductoInline(admin.StackedInline):
    model = Producto
    can_delete = True
    verbose_name_plural = "productos"

class PedidoInline(admin.StackedInline):
    model = Pedido
    can_delete = True
    verbose_name_plural = "pedidos"
    
class ProductoCompradoInline(admin.StackedInline):
    model = ProductoComprado
    can_delete = False
    verbose_name_plural = "productoscomprados"

class ProductoAdmin(UserAdmin):
    inlines = [ ProductoInline, PedidoInline, ProductoCompradoInline]

admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(ProductoComprado)
