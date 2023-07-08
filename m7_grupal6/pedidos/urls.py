from django.urls import path

from . import views

urlpatterns = [
    path("pedidos", views.view_pedidos, name="pedidos"),
    path("pedido_detail/<str:id>", views.pedido_detail, name="pedido_detail"),
    path("pedido_form", views.pedido_form, name="pedido_form"),
    path("pedido_cliente", views.pedido_cliente, name="pedido_cliente")
]