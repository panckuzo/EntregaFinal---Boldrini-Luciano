from django import forms

class Form_Subscriptores(forms.Form):
    mail = forms.EmailField()

class Form_Productos(forms.Form): 
    nombre = forms.CharField(max_length=30)
    categoria = forms.CharField(max_length=30)
    descripcion = forms.CharField(widget=forms.Textarea) 
    precio = forms.IntegerField()
    stock = forms.IntegerField()
    
class Buscar_Producto(forms.Form):
    nombre = forms.CharField(max_length=30, required=False) 
    
class Form_Proveedor(forms.Form):
    nombre = forms.CharField(max_length=50)
    productos= forms.Textarea()
    Telefono = forms.IntegerField()
    mail = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=30)
    
class Buscar_Proveedor(forms.Form):
    ...
    
class Form_Resena(forms.Form):
    nombre_de_cliente= forms.CharField(max_length= 30 )
    resena = forms.Textarea()
    calificacion = forms.IntegerField()
