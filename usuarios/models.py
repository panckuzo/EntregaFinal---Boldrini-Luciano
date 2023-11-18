from django.db import models
from django.contrib.auth.models import User

class Datos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.IntegerField(null=True)
    direccion = models.CharField(max_length=100, null=True)
    ciudad = models.CharField(max_length=100, null=True)
    provincia = models.CharField(max_length=100, null=True)
    fecha_nacimiento = models.DateField(null=True)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
