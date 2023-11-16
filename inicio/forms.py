from django import forms
from ckeditor.fields import RichTextFormField

class Form_Subscriptores(forms.Form):
    mail = forms.EmailField()

class Form_Productos(forms.Form): 
    nombre = forms.CharField(max_length=30)
    categoria = forms.CharField(max_length=30)
    descripcion = RichTextFormField()
    precio = forms.IntegerField()
    stock = forms.IntegerField()
    fecha =  forms.DateField()
    imagen = forms.ImageField(required=False)
    
    
class Buscar_Producto(forms.Form):
    producto_nombre = forms.CharField(max_length=30, required=False) 
    
class Form_Proveedor(forms.Form):
    nombre = forms.CharField(max_length=50)
    productos=  RichTextFormField()
    telefono = forms.IntegerField()
    email = forms.EmailField()
    direccion = forms.CharField(max_length=50)
    
class Buscar_Proveedor(forms.Form):
    proveedor_nombre = forms.CharField(max_length=30, required=False) 
    
class Editar_Producto_Form(forms.Form):
    descripcion = RichTextFormField()
    precio = forms.IntegerField()
    stock = forms.IntegerField()
    imagen = forms.ImageField()
    
class Editar_Proveedor_Form(forms.Form):
    productos = RichTextFormField()
    telefono = forms.IntegerField()
    email = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)

    
class Form_Resena(forms.Form):
    nombre_de_cliente= forms.CharField(max_length= 50 )
    resena = RichTextFormField()
    calificacion = forms.IntegerField()

