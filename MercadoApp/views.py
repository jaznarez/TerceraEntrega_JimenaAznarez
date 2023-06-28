from http.client import HTTPResponse
from django.shortcuts import render
from MercadoApp.models import Cliente
from MercadoApp.forms import formClienteFormulario

def inicio(request):
    return render(request, "MercadoApp/inicio.html")      

def cliente(request):
    return render(request, "MercadoApp/Cliente.html")#tenemos que poner la ruta de donde estamos hasta llegar a Clientes
                                                     #render como tal está hecho para buscar en la carpeta templates (si usamos render, hay que usar carpeta templates)
def Productos(request):
    return render(request, "MercadoApp/Productos.html")

def Pedidos(request):
    return render(request, "MercadoApp/Pedidos.html")

def clienteFormulario(request):
    if request.method =="POST":
        miFormulario = formClienteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            nombre=data["nombre"]
            apellido=data["apellido"]
            email=data["email"]
            telefono=data["telefono"]
            edad=data["edad"]
            cliente = Cliente(nombre=nombre, apellido=apellido,email=email,telefono=telefono,edad=edad)
            cliente.save()
            return render(request, "MercadoApp/inicio.html")
    else:
        miFormulario = formClienteFormulario()

    return render(request, "MercadoApp/clienteFormulario.html", {"miFormulario":miFormulario})#uso un diccionario para crear la variable que necesita clienteForumulario para crear el form para renderizar la pantalla.


    """if request.method =="POST":#metodo POST se relaciona a un forumlario que se genera
        cliente = Cliente(nombre=request.POST["nombre"], apellido=request.POST["apellido"],email=request.POST["email"],telefono=request.POST["telefono"],edad=request.POST["edad"])
        cliente.save()
        return render(request, "MercadoApp/inicio.html")
    return render(request, "MercadoApp/clienteFormulario.html")"""

def getCliente(request):
    return render(request, "MercadoApp/getCliente.html")

def buscarCliente(request):
    if request.GET["email"]:
        email = request.GET["email"]
        cliente = Cliente.objects.filter(email = email)
        return render(request, "MercadoApp/getCliente.html", {"cliente": cliente})
    else:
        respuesta ="No se enviaron datos"
    return HTTPResponse(respuesta)
# Create your views here.
