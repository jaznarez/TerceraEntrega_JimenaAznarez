#from socket import fromshare
from django import forms

class formClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    telefono = forms.IntegerField()
    edad = forms.IntegerField()
