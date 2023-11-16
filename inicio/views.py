from django.shortcuts import render,redirect
from inicio.models import Subscriptores, Productos, Proveedor,Resena
from inicio.forms import Form_Subscriptores, Form_Productos, Form_Resena, Form_Proveedor, Editar_Producto_Form, Editar_Proveedor_Form
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin




# ------------------------- VISTAS CON FUNCIONES --------------------------------------

def inicio(request):
    return render(request, "inicio.html", {})

# def nosotros(request):
#     return render(request, "nosotros.html")



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

# @login_required
def CrearProducto(request):
    if request.method == 'POST':
        formulario = Form_Productos(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data

            nombre = info_limpia.get('nombre')
            categoria = info_limpia.get('categoria')
            descripcion = info_limpia.get('descripcion')
            precio = info_limpia.get('precio')
            stock = info_limpia.get('stock')
            fecha = info_limpia.get('fecha')
            imagen = info_limpia.get('imagen')

            producto = Productos(nombre=nombre,  categoria=categoria,descripcion=descripcion,  precio=precio,stock=stock, fecha=fecha, imagen= imagen)
            producto.save()

            return redirect('crear_producto') 
        else:
            return render(request, 'crear_producto.html', {'formulario': formulario})

    formulario = Form_Productos()
    return render(request, 'crear_producto.html', {'formulario': formulario})

def MostrarProducto(request):
    producto_a_buscar = request.GET.get('producto_nombre')
    

    if producto_a_buscar:
        listado_productos = Productos.objects.filter(producto_nombre__icontains=producto_a_buscar)
    else:
        listado_productos = Productos.objects.all()
        
    
    return render(request, 'productos.html', {'listado_productos':listado_productos})

@login_required
def EliminarProducto(request, producto_id):
    producto_a_eliminar = Productos.objects.get(id=producto_id)
    producto_a_eliminar.delete()
    return redirect("producto")

@login_required
def EditarProducto(request, producto_id):
    producto_a_actualizar = Productos.objects.get(id=producto_id)
    
    if request.method == "POST":
        formulario = Editar_Producto_Form(request.POST, request.FILES)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data

            producto_a_actualizar.producto_descripcion = info_nueva.get('descripcion')
            producto_a_actualizar.producto_precio = info_nueva.get('precio')
            producto_a_actualizar.producto_stock = info_nueva.get('stock')
            producto_a_actualizar.producto_imagen = info_nueva.get('imagen')
            
            producto_a_actualizar.save()
            return redirect('productos')
        else:
            return render(request, 'actualizar_producto.html', {'formulario': formulario})
    else:
        formulario = Editar_Producto_Form(initial={
            'descripcion': producto_a_actualizar.producto_descripcion,
            'precio': producto_a_actualizar.producto_precio,
            'stock': producto_a_actualizar.producto_stock,
            'imagen':producto_a_actualizar.producto_imagen 
        })
    return render(request, 'actualizar_producto.html', {'formulario': formulario})


def DetalleProducto(request, producto_id):
    producto = Productos.objects.get(id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})


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
        todas_las_resenas = Resena.objects.all()
        return render(request, 'resenas.html', {'formulario': formulario_resena, 'resenas': todas_las_resenas})


# ----------------------------- CLASES BASADAS EN VISTAS ------------------------------------

class CrearProveedor(LoginRequiredMixin, CreateView):
    model = Proveedor
    template_name = "crear_proveedor.html"
    fields = ['proveedor_nombre', 'proveedor_productos', 'proveedor_telefono', 'proveedor_mail', 'proveedor_direccion']
    success_url = reverse_lazy('proveedor')
    
class MostrarProveedor(ListView):
    model = Proveedor
    context_object_name = 'listado_de_Proveedores'
    template_name = 'proveedor.html'
    
    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        if nombre:
            listado_de_proveedores = self.model.objects.filter(nombre__icontains=nombre)
        else:
            listado_de_proveedores = self.model.objects.all()
        return listado_de_proveedores


class EditarProveedor(LoginRequiredMixin, UpdateView):
    model = Proveedor
    template_name = "actualizar_proveedor.html"
    fields = ['proveedor_productos', 'proveedor_telefono', 'proveedor_mail', 'proveedor_direccion']
    success_url = reverse_lazy('proveedor')


class DetalleProveedor(DetailView):
    model = Proveedor
    template_name = "detalle_proveedor.html"


class EliminarProveedor(LoginRequiredMixin, DeleteView):
    model = Proveedor
    template_name = "eliminar_proveedor.html"
    success_url = reverse_lazy('proveedor')
    
    







# @login_required
# def Eliminar_Proveedor(request, proveedor_id):
#     proveeedor_a_eliminar = Proveedor.objects.get(id=proveedor_id)
#     proveeedor_a_eliminar.delete()
#     return redirect("producto")

# @login_required
# def Editar_Proveedor(request, proveedor_id):
#     proveedor_a_actualizar = Proveedor.objects.get(id=proveedor_id)
    
#     if request.method == "POST":
#         formulario = Editar_Proveedor_Form(request.POST)
#         if formulario.is_valid():
#             info_nueva = formulario.cleaned_data

#             proveedor_a_actualizar.proveedor_productos = info_nueva.get('productos')
#             proveedor_a_actualizar.proveedor_telefono = info_nueva.get('telefono')
#             proveedor_a_actualizar.proveedor_mail = info_nueva.get('mail')
#             proveedor_a_actualizar.proveedor_direccion = info_nueva.get('direccion')
            
#             proveedor_a_actualizar.save()
#             return redirect('proveedor')
#         else:
#             return render(request, 'actualizar_proveedor.html', {'formulario': formulario})
#     else:
#         formulario = Editar_Producto_Form(initial={
#             'productos': proveedor_a_actualizar.proveedor_productos,
#             'telefono': proveedor_a_actualizar.proveedor_telefono,
#             'mail': proveedor_a_actualizar.proveedor_mail,
#             'direccion':proveedor_a_actualizar.proveedor_direccion 
#         })
#     return render(request, 'actualizar_proveedor.html', {'formulario': formulario})

# def Detalle_Proveedor(request, proveedor_id):
#     proveedor = Proveedor.objects.get(id=proveedor_id)
#     return render(request, 'detalle_proveedor.html', {'proveedor': proveedor})


