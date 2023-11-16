from django.db import models
from ckeditor.fields import RichTextField
from datetime import date


class Subscriptores(models.Model): 
    mail = models.EmailField()
    
class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    descripcion = RichTextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    fecha =  models.DateField(default=date.today)
    imagen = models.ImageField(upload_to='productos_img', null=True,blank=True )
    
    def __str__(self):
        return f'{self.id} - Nombre: {self.nombre}'

        
class Proveedor(models.Model):
    proveedor_nombre = models.CharField(max_length=50)
    proveedor_productos= RichTextField()
    proveedor_telefono = models.IntegerField(max_length=30)
    proveedor_mail = models.EmailField()
    proveedor_direccion = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.id} - Nombre: {self.proveedor_nombre}'
    
class Resena(models.Model):
    nombre_de_cliente= models.CharField(max_length=50)
    resena = RichTextField()
    calificacion = models.IntegerField()


