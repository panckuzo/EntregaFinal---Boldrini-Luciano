from django.db import models

class Subscriptores(models.Model): 
    mail = models.CharField(max_length=50)
    
class Productos(models.Model): 
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)
    descripcion = models.TextField()
    precio= models.IntegerField()
    stock= models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.categoria} - {self.nombre}'
    
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    productos= models.TextField()
    Telefono = models.IntegerField(max_length=30)
    mail = models.CharField(max_length=50)
    direccion = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nombre} - {self.telefono} - {self.mail} - {self.direccion}'
    
class Resena(models.Model):
    nombre_de_cliente= models.IntegerField(max_length=30)
    resena = models.TextField()
    calificacion = models.IntegerField(max_length=2)


