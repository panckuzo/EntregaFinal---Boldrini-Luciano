from django.urls import path
from inicio.views import inicio, nosotros, shop

urlpatterns = [
    path('', inicio, name="inicio"),
    path('nosotros', nosotros, name="nosotros"),
    path('shop', shop, name="shop")
    ]