from django.db import models

class Subscriptores(models.Model): 
    mail = models.EmailField()
    
class Productos(models.Model):
    producto_nombre = models.CharField(max_length=30)
    producto_categoria = models.CharField(max_length=30)
    producto_descripcion = models.TextField()
    producto_precio = models.IntegerField()
    producto_stock = models.IntegerField()
    def __str__(self):
        return f'{self.id}--   {self.producto_nombre} - {self.producto_categoria} - {self.producto_descripcion} - {self.producto_precio} - {self.producto_stock}'

        
class Proveedor(models.Model):
    proveedor_nombre = models.CharField(max_length=50)
    proveedor_productos= models.TextField()
    proveedor_telefono = models.IntegerField(max_length=30)
    proveedor_mail = models.CharField(max_length=50)
    proveedor_direccion = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.id}--   {self.proveedor_nombre} - {self.proveedor_productos} - {self.proveedor_telefono} - {self.proveedor_mail} - {self.proveedor_direccion}'
    
class Resena(models.Model):
    nombre_de_cliente= models.CharField(max_length=50)
    resena = models.TextField()
    calificacion = models.IntegerField()


