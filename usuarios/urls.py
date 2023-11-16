from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import InicioSesion, registro, editar_perfil, CambiarPassword
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', InicioSesion, name='inicio_sesion'),
    path('logout/', LogoutView.as_view(template_name='cuentas/cerrar_sesion.html'), name='cerrar_seseio'),
    path('registro/', registro, name='registro'),
    # path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/editar/password/', CambiarPassword.as_view(), name='cambiar_password')
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

