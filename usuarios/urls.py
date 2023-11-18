from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import InicioSesion, CambiarPassword, Registro, Perfil, EditarPerfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', InicioSesion, name='inicio_sesion'),
    path('logout/', LogoutView.as_view(template_name='cuentas/cerrar_sesion.html'), name='cerrar_sesion'),
    path('registro/', Registro, name='registro'),
    path('perfil/', Perfil.as_view(), name='perfil'),
    path('perfil/editar/', EditarPerfil, name='editar_perfil'),
    path('perfil/editar/password/', CambiarPassword.as_view(), name='cambiar_password')
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
