from django.shortcuts import render,redirect
from inicio.models import Subscriptores, Productos, Proveedor,Resena
from inicio.forms import Form_Subscriptores, Form_Productos, Form_Resena, Buscar_Producto


def inicio(request):
    return render(request, "inicio.html", {})

def nosotros(request):
    return render(request, "nosotros.html")

def shop(request):
    return render(request, "shop.html")

def producto(request):
    return render(request, "productos.html")

def crear(request):
    return render(request, "crear.html")

def resena(request):
    return render(request, "resenas.html")


def CrearProducto(request):
    if request.method == 'POST':
        formulario_prod = Form_Productos(request.POST)
        if formulario_prod.is_valid():
            infolimpia=formulario_prod.cleaned_data
            
            nombre = infolimpia.get('nombre')
            categoria = infolimpia.get('categoria')
            descripcion = infolimpia.get('descripcion')
            precio = infolimpia.get('precio')
            stock = infolimpia.get('stock')
            
            Productos = Productos(nombre=nombre,categoria=categoria, descripcion=descripcion, precio=precio, stock=stock)
            Productos.save()
            
            return redirect('shop')
        
        else:
            return render(request, 'inicio/crear.html', {'formulario': formulario_prod})
    else:
        formulario_prod = Form_Productos()
        return render(request, 'inicio/crear.html', {'formulario': formulario_prod})
    
def Producto(request):
    formulario = Buscar_Producto(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre')
        listado_de_productos = Producto.objects.filter(nombre__icontains=nombre_a_buscar)
    
    formulario = Buscar_Producto()
    return render(request, 'inicio/productos.html', {'formulario': formulario, 'listado_de_productos': listado_de_productos})
    


