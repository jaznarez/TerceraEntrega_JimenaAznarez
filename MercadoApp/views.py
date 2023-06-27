from http.client import HTTPResponse
from django.shortcuts import render
from MercadoApp.models import Cliente

def inicio(request):
    return render(request, "MercadoApp/inicio.html")      

def Cliente(request):
    return render(request, "MercadoApp/Cliente.html")#tenemos que poner la ruta de donde estamos hasta llegar a Clientes
                                                     #render como tal está hecho para buscar en la carpeta templates (si usamos render, hay que usar carpeta templates)
def Productos(request):
    return render(request, "MercadoApp/Productos.html")

def Pedidos(request):
    return render(request, "MercadoApp/Pedidos.html")

def clienteFormulario(request):
    if request.method =="POST":#metodo POST se relaciona a un forumlario que se genera
        cliente = Cliente(nombre=request.POST["Nombre"], apellido=request.POST["Apellido"],email=request.POST["Email"],telefono=request.POST["Telefono"],edad=request.POST["Edad"])
        cliente.save()
        return render(request, "MercadoApp/inicio.html")
    return render(request, "MercadoApp/clienteFormulario.html")


# Create your views here.
