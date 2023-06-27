from socket import fromshare
from django import forms

class clienteFormulario(forms, Form):
    usuario = forms.CharField()
    contraseña = forms.CharField()
    
