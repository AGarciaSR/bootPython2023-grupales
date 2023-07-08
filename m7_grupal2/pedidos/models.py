import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    sku = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    precio = models.FloatField(null=False)
    stock = models.IntegerField(default=0)

class Pedido(models.Model):
    class EstadoPedido(models.Choices):
        INGRESADO = "Ingresado"
        PREPARANDO = "Preparando"
        ENVIADO = "Enviado"
        RECIBIDO = "Recibido"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(User, related_name="User", on_delete=models.CASCADE)
    dir_entrega = models.CharField(max_length=400, null=False)
    productos = models.CharField(max_length=400, verbose_name="Productos")
    forma_pago = models.CharField(max_length=40)
    estado = models.CharField(choices=EstadoPedido.choices, default="Ingresado")
    gestionado = models.BooleanField(editable=False)