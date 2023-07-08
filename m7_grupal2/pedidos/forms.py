from django import forms
from django.contrib.auth.models import User
from .models import Pedido

class PedidoForm(forms.Form):
    usuario = forms.ModelChoiceField(queryset=User.objects.all(), blank=True, required=True)
    dir_entrega = forms.CharField(max_length=400, required=True)
    forma_pago = forms.CharField(max_length=40, required=True)
    productos = forms.CharField(max_length=400, required=True)