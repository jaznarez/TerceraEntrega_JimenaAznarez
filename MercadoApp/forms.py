#from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class formClienteFormulario(forms.Form): #generamos la instancia de formulario
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    telefono = forms.IntegerField()
    edad = forms.IntegerField()

class UserEditForm(UserChangeForm):
    username= forms.CharField(widget= forms.TextInput(attrs={"placeholder": "Username"}))
    email= forms.CharField(widget= forms.TextInput(attrs={"placeholder": "Email"}))
    first_name= forms.CharField(widget= forms.TextInput(attrs={"placeholder": "First Name"}))
    last_name= forms.CharField(widget= forms.TextInput(attrs={"placeholder": "Last Name"}))
    password= forms.CharField(widget= forms.PasswordInput(attrs={"placeholder": "Password"}))

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]
        help_texts = {k:"" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password= forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Old Password"}))
    old_password1= forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "New Password"}))
    old_password2= forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Confirmation New Password"}))

    
    class Meta:
        model = User
        fields = ["old_password", "old_password1", "old_password"]
        help_texts = {k:"" for k in fields}