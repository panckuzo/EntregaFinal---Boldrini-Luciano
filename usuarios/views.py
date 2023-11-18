from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from usuarios.forms import CrearUsuarioForm, EditarPerfilForm, CambiarPasswordForm, MiAuthenticationForm
from usuarios.models import Datos, User


def Registro(request):
    formulario = CrearUsuarioForm()
    
    if request.method == 'POST':
        formulario = CrearUsuarioForm(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('inicio_sesion')
            
    return render(request, 'cuentas/registro.html', {'form': formulario})

def InicioSesion(request):
    
    formulario = MiAuthenticationForm()
    
    if request.method == 'POST':
        formulario = MiAuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasena = formulario.cleaned_data.get('password')

            user = authenticate(request, username=usuario, password=contrasena)
            
            login(request, user)
            
            Datos.objects.get_or_create(user=request.user)
            
            return redirect('perfil')

    return render(request, 'cuentas/inicio_sesion.html', {'form': formulario})

def EditarPerfil(request):
    
    datos = request.user.datos
    
    formulario = EditarPerfilForm(instance=request.user, initial={'telefono': datos.telefono,'direccion': datos.direccion, 'ciudad': datos.ciudad,'provincia': datos.provincia,'fecha_nacimiento': datos.fecha_nacimiento,'avatar': datos.avatar})
    

    if request.method == 'POST':
        formulario = EditarPerfilForm(request.POST, request.FILES, instance=request.user)

        if formulario.is_valid():
            
            nueva_telefono = formulario.cleaned_data.get('telefono')
            nueva_direccion = formulario.cleaned_data.get('direccion')
            nueva_ciudad = formulario.cleaned_data.get('ciudad')
            nueva_provincia = formulario.cleaned_data.get('provincia')
            nueva_fecha_nacimiento = formulario.cleaned_data.get('fecha_nacimiento')
            nueva_avatar = formulario.cleaned_data.get('avatar')
            
            if nueva_telefono:
                datos.telefono = nueva_telefono
            if nueva_direccion:
                datos.direccion = nueva_direccion
            if nueva_ciudad:
                datos.ciudad = nueva_ciudad
            if nueva_provincia:
                datos.provincia = nueva_provincia
            if nueva_fecha_nacimiento:
                datos.fecha_nacimiento = nueva_fecha_nacimiento
            if nueva_avatar:
                datos.avatar = nueva_avatar
            
            datos.save()
            formulario.save()

            return redirect('perfil')

    return render(request, 'cuentas/editar_perfil.html', {'form': formulario})



class Perfil(ListView):
    model = User
    template_name = 'cuentas/perfil.html'


class CambiarPassword(PasswordChangeView):
    template_name = 'cuentas/cambiar_password.html'
    success_url = reverse_lazy('perfil')
    form_class = CambiarPasswordForm
