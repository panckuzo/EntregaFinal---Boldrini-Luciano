from django import forms

class Form_Subscriptores(forms.Form):
    mail = forms.EmailField()

class Form_Productos(forms.Form): 
    producto_nombre = forms.CharField(max_length=30)
    producto_categoria = forms.CharField(max_length=30)
    producto_descripcion = forms.CharField(widget=forms.Textarea) 
    producto_precio = forms.IntegerField()
    producto_stock = forms.IntegerField()
    
class Buscar_Producto(forms.Form):
    producto_nombre = forms.CharField(max_length=30, required=False) 
    
class Form_Proveedor(forms.Form):
    proveedor_nombre = forms.CharField(max_length=50)
    proveedor_productos= forms.CharField(widget=forms.Textarea) 
    proveedor_telefono = forms.IntegerField()
    proveedor_mail = forms.CharField(max_length=50)
    proveedor_direccion = forms.CharField(max_length=30)
    
class Buscar_Proveedor(forms.Form):
    proveedor_nombre = forms.CharField(max_length=30, required=False) 
    
class Form_Resena(forms.Form):
    nombre_de_cliente= forms.CharField(max_length= 50 )
    resena = forms.CharField(widget=forms.Textarea) 
    calificacion = forms.IntegerField()

