from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    edad = models.IntegerField(null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        AppUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.appuser.save()
    
    
class Proveedor(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200, null=True)
    telefono = models.IntegerField(null=True)
    
    def __str__(self):
        return self.nombre