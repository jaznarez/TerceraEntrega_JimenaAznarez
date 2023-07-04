from http.client import HTTPResponse
from django.shortcuts import render
from MercadoApp.models import Cliente
from MercadoApp.forms import formClienteFormulario, UserEditForm, ChangePasswordForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required #sirve para pedir el login obligatorio, si no la pagina no funciona. se escribe @login_required arriba de cada accion que querramos necesite login
from django.contrib.auth.models import User



def inicio(request):
    return render(request, "MercadoApp/inicio.html")      

def cliente(request):
    Clientes = Cliente.objects.all() #pido toda la informacion que tenga Cliente alojada en su base de datos
    return render(request, "MercadoApp/Cliente.html", {"Clientes": Clientes}) #genera una lista con los datos de todos los clientes, y que podemos usar luego en el template Clientes

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


#def leerClientes(request):
    
def loginWeb(request): #ojo no puede llamarse solo login porque ya estoy importantdo una funcion con ese nombre.
    if request.method == "POST":
        user = authenticate(username=request.POST["user"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return render(request, "MercadoApp/inicio.html")
        else:
            return render(request, "MercadoApp/login.html", {"error": "Usuario o contraseña incorrectos"})
    else:
        return render(request, "MercadoApp/login.html")

def registro(request):
    if request.method == "POST":
        userCreate = UserCreationForm(request.POST) #CREA INSTANCIA DE FORMULARIO EN BASE AL FORMULARIO QUE TENEMOS CREADO
        if userCreate is not None:

            userCreate.save()

            return render(request, 'MercadoApp/login.html')

    else:

        return render(request, 'MercadoApp/registro.html')

@login_required
def perfilview(request):
    return render(request, 'MercadoApp/Perfil/Perfil.html')

@login_required
def editarPerfil(request):
    usuario = request.user
    user_basic_info = User.objects.get(id = usuario.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance= usuario)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get("username")
            user_basic_info.email = form.cleaned_data.get("email")
            user_basic_info.first_name= form.cleaned_data.get("first_name")
            user_basic_info.last_name= form.cleaned_data.get("last_name")
            user_basic_info.save()
            return render(request, "MercadoApp/Perfil/Perfil.html")
    else:
        form = UserEditForm(initial= {"username": usuario.username, "email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name})
        return render(request, "MercadoApp/Perfil/editarPerfil.html", {"form": form})   
     
     
@login_required
def changePassword(request):
    usuario = request.user
    if request.method == "POST":
        form = ChangePasswordForm(data = request.POST, user = usuario)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, "MercadoApp/inicio.html")
    else:
        form = ChangePasswordForm(user = usuario)
        return render(request, "MercadoApp/Perfil/changePassword.html", {"form": form})

def editAvatar(request):
    pass 