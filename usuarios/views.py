from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from usuarios.forms import CrearUsuarioForm, EdicionPerfilForm, LoginForm



def InicioSesion(request):
    
    formulario = LoginForm()
    
    if request.method == 'POST':
        formulario = LoginForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('usuario')
            contra = formulario.cleaned_data.get('contraseña')

            user = authenticate(username=usuario, password=contra)
            
            
            
            return redirect('editar_perfil')

    return render(request, 'cuentas/inicio_sesion.html', {'form': formulario})

def registro(request):
    formulario = CrearUsuarioForm()
    
    if request.method == 'POST':
        formulario = CrearUsuarioForm(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('inicio_sesion')
            
    return render(request, 'cuentas/registro.html', {'form': formulario})



class CambiarPassword(PasswordChangeView):
    template_name = 'cuentas/cambiar_password.html'
    success_url = reverse_lazy('perfil')