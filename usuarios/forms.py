from django import forms

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CrearUsuarioForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuario', widget=forms.TextInput())
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())

