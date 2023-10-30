from django.urls import path
from inicio.views import inicio, shop, crear, resena, producto

urlpatterns = [
    path('', inicio, name="inicio"),
    path('producto', producto, name="producto"),
    path('shop', shop, name="shop"),
    path('crear', crear, name="crear"),
    path('Reseña', resena, name="resena"),
    ]
    