from django import forms
from .models import Proveedor

class ProveedorForm(forms.Form):
    rut = forms.CharField(max_length=10)
    nombre = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=200)
    telefono = forms.IntegerField()
    class Meta:
        model = Proveedor
        fields = '__all__'