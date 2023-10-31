from django.urls import path
from inicio.views import inicio, shop, Productos, CrearResena, Crear, Mostrar, Subscriptores, Subscriptor

urlpatterns = [
    path('', Subscriptor, name="inicio"),
    path('producto', Mostrar, name="producto"),
    path('shop', shop, name="shop"),
    path('crear', Crear, name="crear"),
    path('reseña', CrearResena, name="resena"),
    ]
    