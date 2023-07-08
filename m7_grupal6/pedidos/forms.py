from django import forms
from django.contrib.auth.models import User
from .models import Pedido, Producto

class PedidoForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=User.objects.all(), blank=True, required=True)
    dir_entrega = forms.CharField(max_length=400, required=True)
    forma_pago = forms.CharField(max_length=40, required=True)
    productos = forms.CharField(max_length=400, required=True)
    
class ActualizaPedido(forms.Form):
    ESTADO_CHOICES =(
        ("Ingresado", "Ingresado"),
        ("Preparando", "Preparando"),
        ("Enviado", "Enviado"),
        ("Recibido", "Recibido"),
    )
    id = forms.CharField()
    estado = forms.ChoiceField(choices = ESTADO_CHOICES)
    
class ClientePedido(forms.Form):
    dir_entrega = forms.CharField(max_length=400, required=True)
    forma_pago = forms.CharField(max_length=40, required=True)
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), blank=True, required=True)
    cantidad = forms.IntegerField()