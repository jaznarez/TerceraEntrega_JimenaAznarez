from http.client import HTTPResponse
from django.shortcuts import render

def inicio(request):
    return render(request, "MercadoApp/inicio.html")      
                                                 
def Cliente(request):
    return render(request, "MercadoApp/Cliente.html")#tenemos que poner la ruta de donde estamos hasta llegar a Clientes
                                                     #render como tal está hecho para buscar en la carpeta templates (si usamos render, hay que usar carpeta templates)
def Productos(request):
    return render(request, "MercadoApp/Productos.html")

def Pedidos(request):
    return render(request, "MercadoApp/Pedidos.html")


# Create your views here.
