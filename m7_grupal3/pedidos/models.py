import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    sku = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    precio = models.FloatField(null=False)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.nombre} ({self.sku})"

class Pedido(models.Model):
    class EstadoPedido(models.Choices):
        INGRESADO = "Ingresado"
        PREPARANDO = "Preparando"
        ENVIADO = "Enviado"
        RECIBIDO = "Recibido"
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(User, related_name="User", on_delete=models.CASCADE)
    dir_entrega = models.CharField(max_length=400, null=False)
    forma_pago = models.CharField(max_length=40)
    estado = models.CharField(choices=EstadoPedido.choices, default="Ingresado")
    gestionado = models.BooleanField(editable=False)
    
    def __str__(self):
        return f"{str(self.id)} -- {self.usuario.first_name} {self.usuario.last_name}"
    
class ProductoComprado(models.Model):
    comprado = models.ForeignKey(Producto, related_name="Producto", on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, related_name="Pedido", null=True, on_delete=models.SET_NULL)
    cantidad = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{str(self.pedido.id)} -- {self.pedido.usuario.first_name} {self.pedido.usuario.last_name} -- {self.comprado.nombre}"