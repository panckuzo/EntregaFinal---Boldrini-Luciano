from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django.contrib.auth.models import User

class CrearUsuarioForm(UserCreationForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
        
class MiAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    
class EditarPerfilForm(UserChangeForm):
    password = None
    email = forms.EmailField(label='Email', required=False)
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    telefono = forms.IntegerField(required=False)
    direccion = forms.CharField(max_length=100,required=False)
    ciudad = forms.CharField(max_length=100,required=False)
    provincia = forms.CharField(max_length=100,required=False)
    fecha_nacimiento = forms.DateField(required=False)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'telefono', 'direccion', 'ciudad', 'provincia', 'fecha_nacimiento', 'avatar']
    

class CambiarPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña actual', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirmar nueva contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {key: '' for key in fields}



