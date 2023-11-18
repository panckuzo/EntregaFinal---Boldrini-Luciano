from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from inicio.views import  CrearResena, CrearProducto, CrearProveedor,  MostrarProducto, MostrarProveedor, Subscriptor, EliminarProducto, EditarProducto, DetalleProducto, EliminarProveedor, EditarProveedor, DetalleProveedor, About_me


urlpatterns = [
    path('', Subscriptor, name='inicio'),
    
    path('producto/', MostrarProducto, name='producto'),
    path('crear_producto/', CrearProducto, name="crear_producto"),
    path('producto/<int:producto_id>/', DetalleProducto, name='detalle_producto'),
    path('producto/<int:producto_id>/eliminar/', EliminarProducto, name='eliminar_producto'),
    path('producto/<int:producto_id>/actualizar/', EditarProducto, name='actualizar_producto'),
    
    path('proveedor/', MostrarProveedor.as_view(), name = 'proveedor'),
    path('crear_proveedor/', CrearProveedor.as_view(), name='crear_proveedor'),
    path('proveedor/<int:pk>/', DetalleProveedor.as_view(), name='detalle_proveedor'),
    path('proveedor/<int:pk>/eliminar/', EliminarProveedor.as_view(), name='eliminar_proveedor'),
    path('proveedor/<int:pk>/actualizar/', EditarProveedor.as_view(), name='actualizar_proveedor'),
    
    path('reseña/', CrearResena, name='resena'),
    
    path('about_me/', About_me, name='about_me'),
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)