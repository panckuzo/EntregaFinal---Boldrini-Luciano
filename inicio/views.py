from django.shortcuts import render,redirect
from inicio.models import Subscriptores, Productos, Proveedor,Resena
from inicio.forms import Form_Subscriptores, Form_Productos, Form_Resena, Buscar_Producto, Form_Proveedor, Form_Productos, Buscar_Proveedor


def inicio(request):
    return render(request, "inicio.html", {})

# def nosotros(request):
#     return render(request, "nosotros.html")

def shop(request):
    return render(request, "shop.html")

def Subscriptor(request):
    if request.method == 'POST':
        formulario = Form_Subscriptores(request.POST)
        if formulario.is_valid():
            mail = formulario.cleaned_data['mail']
            subscriptor = Subscriptores(mail=mail)
            subscriptor.save()
            return redirect('inicio')
    else:
        formulario = Form_Subscriptores()
    return render(request, 'inicio.html', {'formulario': formulario})

def producto(request):
    return render(request, "productos.html")

def crear(request):
    return render(request, "crear.html")

def resena(request):
    return render(request, "resenas.html")

def Crear(request):
    if request.method == 'POST':
        if 'producto_nombre' in request.POST:
            formulario_prod = Form_Productos(request.POST)
            if formulario_prod.is_valid():
                producto_nombre = formulario_prod.cleaned_data['producto_nombre']
                producto_categoria = formulario_prod.cleaned_data['producto_categoria']
                producto_descripcion = formulario_prod.cleaned_data['producto_descripcion']
                producto_precio = formulario_prod.cleaned_data['producto_precio']
                producto_stock = formulario_prod.cleaned_data['producto_stock']

                producto = Productos(producto_nombre=producto_nombre, producto_categoria=producto_categoria,producto_descripcion=producto_descripcion, producto_precio=producto_precio,producto_stock=producto_stock)
                producto.save()
                return redirect('crear') 
            else:
                return render(request, 'crear.html', {'formulario_prod': formulario_prod})

        elif 'proveedor_nombre' in request.POST:
            formulario_proveedor = Form_Proveedor(request.POST)
            if formulario_proveedor.is_valid():
                proveedor_nombre = formulario_proveedor.cleaned_data['proveedor_nombre']
                proveedor_productos = formulario_proveedor.cleaned_data['proveedor_productos']
                proveedor_telefono = formulario_proveedor.cleaned_data['proveedor_telefono']
                proveedor_mail = formulario_proveedor.cleaned_data['proveedor_mail']
                proveedor_direccion = formulario_proveedor.cleaned_data['proveedor_direccion']

                proveedor = Proveedor(proveedor_nombre=proveedor_nombre, proveedor_productos=proveedor_productos, proveedor_telefono=proveedor_telefono, proveedor_mail=proveedor_mail, proveedor_direccion=proveedor_direccion)
                proveedor.save()
                return redirect('crear')  
            else:
                return render(request, 'crear.html', {'formulario_proveedor': formulario_proveedor})
    else:
        formulario_prod = Form_Productos()
        formulario_proveedor = Form_Proveedor()
        return render(request, 'crear.html', {'formulario_prod': formulario_prod, 'formulario_proveedor': formulario_proveedor})

def Mostrar(request):
    producto_a_buscar = request.GET.get('producto_nombre')
    proveedor_a_buscar = request.GET.get('proveedor_nombre')

    if producto_a_buscar:
        listado_productos = Productos.objects.filter(producto_nombre__icontains=producto_a_buscar)
    else:
        listado_productos = Productos.objects.all()
        
    if proveedor_a_buscar:
        listado_proveedores = Proveedor.objects.filter(proveedor_nombre__icontains=proveedor_a_buscar)
    else:
        listado_proveedores = Proveedor.objects.all()

    return render(request, 'productos.html', {'listado_productos':listado_productos, 'listado_proveedores':listado_proveedores})


def CrearResena(request):
    if request.method == 'POST':
        formulario_resena= Form_Resena(request.POST)
        if formulario_resena.is_valid():
            nombre_de_cliente = formulario_resena.cleaned_data['nombre_de_cliente']
            resena = formulario_resena.cleaned_data['resena']
            calificacion = formulario_resena.cleaned_data['calificacion']
            
            resena = Resena(nombre_de_cliente=nombre_de_cliente, resena=resena, calificacion=calificacion)
            resena.save()
            return redirect('resena') 

        else:
            return render(request, 'resenas.html', {'formulario': formulario_resena})
    else:
        formulario_resena= Form_Resena()
        # Recuperar todas las reseñas
        todas_las_resenas = Resena.objects.all()
        return render(request, 'resenas.html', {'formulario': formulario_resena, 'resenas': todas_las_resenas})




