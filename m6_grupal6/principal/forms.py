from django import forms
from django.contrib.auth.models import User, Group

class UserForm(forms.ModelForm):
    username = forms.CharField(label="Nombre de usuario", max_length=20, required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    email = forms.EmailField()
    edad = forms.IntegerField(label="Edad")
    ciudad = forms.CharField(label="Ciudad", max_length=100)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), blank=True, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'edad', 'ciudad', 'group']