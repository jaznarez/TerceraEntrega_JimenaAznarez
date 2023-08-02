from http.client import HTTPResponse
from turtle import home
from django.template import loader
from django.shortcuts import render, redirect
from MercadoApp.models import *
from MercadoApp.forms import formClienteFormulario, UserEditForm, ChangePasswordForm, AvatarForm, formPedidoFormulario, CommentForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required #sirve para pedir el login obligatorio, si no la pagina no funciona. se escribe @login_required arriba de cada accion que querramos necesite login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


@login_required
def inicio(request):
    avatar = getavatar(request)
    return render(request, "MercadoApp/inicio.html", {"avatar":avatar}) #mandamos el avatar en manera de diccionario para poder acceder en la web   

def cliente(request):
    avatar = getavatar(request)
    Clientes = Cliente.objects.all() #pido toda la informacion que tenga Cliente alojada en su base de datos
    return render(request, "MercadoApp/Cliente.html", {"Clientes":Clientes, "avatar":avatar}) #genera una lista con los datos de todos los clientes, y que podemos usar luego en el template Clientes

def productos(request):
    avatar = getavatar(request)
    Producto = Productos.objects.all()
    return render(request, "MercadoApp/Productos.html", {"avatar":avatar})

def pedidos(request):
    avatar = getavatar(request)
    Pedido = Pedidos.objects.all()
    return render(request, "MercadoApp/Pedidos.html", {"Pedidos":Pedido, "avatar":avatar})

def clienteFormulario(request):
    Clientes = Cliente.objects.all() #pido toda la informacion que tenga Cliente alojada en su base de datos
    avatar = getavatar(request)
    #return render(request, "MercadoApp/Cliente.html", {"Clientes": Clientes}) #genera una lista con los datos de todos los clientes, y que podemos usar luego en el template Clientes
    if request.method =="POST":
        cliente = Cliente(nombre=request.POST["nombre"], apellido=request.POST["apellido"],email=request.POST["email"],telefono=request.POST["telefono"],edad=request.POST["edad"])
        cliente.save()
        miFormulario = formClienteFormulario() #para que se limpien los datos del formulario una vez que ya cargo un cliente
        return render(request, "MercadoApp/clienteFormulario.html", {"miFormulario":miFormulario, "Clientes": Clientes, "avatar":avatar})
    else:
        miFormulario = formClienteFormulario()
    return render(request, "MercadoApp/clienteFormulario.html", {"miFormulario":miFormulario, "Clientes": Clientes, "avatar":avatar})#uso un diccionario para crear la variable que necesita clienteForumulario para crear el form para renderizar la pantalla.

def pedidosFormulario(request):
    Pedido = Pedidos.objects.all() #pido toda la informacion que tenga Pedidos alojada en su base de datos
    avatar = getavatar(request)
    #return render(request, "MercadoApp/Cliente.html", {"Clientes": Clientes}) #genera una lista con los datos de todos los clientes, y que podemos usar luego en el template Clientes
    if request.method =="POST":
        pedido = Pedidos(numero_pedido=request.POST["numero_pedido"], nombre_producto=request.POST["nombre_producto"], categoria_producto=request.POST["categoria_producto"],cantidad=request.POST["cantidad"], fecha_entrega=request.POST["fecha_entrega"])
        pedido.save()
        miFormulario = formPedidoFormulario() #para que se limpien los datos del formulario una vez que ya cargo un pedido
        return redirect('Pedidos')
        #return render(request, "MercadoApp/pedidosFormulario.html", {"miFormulario":miFormulario, "Pedido": Pedido, "avatar":avatar})
    else:
        miFormulario = formPedidoFormulario()
    return render(request, "MercadoApp/pedidosFormulario.html", {"miFormulario":miFormulario, "Pedido": Pedido, "avatar":avatar})#uso un diccionario para crear la variable que necesita clienteForumulario para crear el form para renderizar la pantalla.


    """if request.method =="POST":#metodo POST se relaciona a un forumlario que se genera
        cliente = Cliente(nombre=request.POST["nombre"], apellido=request.POST["apellido"],email=request.POST["email"],telefono=request.POST["telefono"],edad=request.POST["edad"])
        cliente.save()
        return render(request, "MercadoApp/inicio.html")
    return render(request, "MercadoApp/clienteFormulario.html")"""

def getCliente(request):
    return render(request, "MercadoApp/getCliente.html")

def getPedido(request): 
    return render(request, "MercadoApp/getPedido.html")

def getProducto(request):
    return render(request, "MercadoApp/Productos.html")

def buscarCliente(request):
    avatar = getavatar(request)
    if request.GET["email"]:
        email = request.GET["email"]
        cliente = Cliente.objects.filter(email = email)
        return render(request, "MercadoApp/getCliente.html", {"cliente": cliente, "avatar":avatar})
    else:
        respuesta ="No se enviaron datos"
    return HTTPResponse(respuesta)

def eliminarCliente(request, nombre_cliente):
    avatar = getavatar(request)
    cliente = Cliente.objects.get(nombre=nombre_cliente)
    cliente.delete()
    miFormulario = formClienteFormulario()
    Clientes = Cliente.objects.all()
    return render(request, "MercadoApp/clienteFormulario.html", {"miFormulario":miFormulario, "Clientes": Clientes, "avatar":avatar})

def editarCliente(request, nombre_cliente):
    avatar = getavatar(request)
    cliente = get_object_or_404(Cliente, nombre= nombre_cliente)
    if request.method == "POST" :#validar si es un cliente valido
        miFormulario = formClienteFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            cliente.nombre = data["nombre"]
            cliente.apellido = data["apellido"]
            cliente.email = data["email"]
            cliente.telefono = data["telefono"]
            cliente.edad = data["edad"]
            cliente.save()
            #miFormulario = formClienteFormulario()
            #Clientes = Cliente.objects.all()
            #return render(request, "MercadoApp/clienteFormulario.html", {"miFormulario":miFormulario, "Clientes": Clientes, "avatar":avatar})
            return redirect('Cliente')
    else:
        miFormulario = formClienteFormulario(initial={"nombre": cliente.nombre, "apellido": cliente.apellido, "email":cliente.email, "telefono": cliente.telefono, "edad":cliente.edad})
    return render(request, "MercadoApp/editarCliente.html", {"miFormulario":miFormulario, "cliente": nombre_cliente, "avatar":avatar})

def buscarPedido(request):
    avatar = getavatar(request)
    if request.GET["numero_pedido"]:
        numero = request.GET["numero_pedido"]
        pedido = Pedidos.objects.filter(numero_pedido = numero)
        return render(request, "MercadoApp/getPedido.html", {"pedido": pedido, "avatar":avatar})
    else:
        respuesta ="No se enviaron datos"
    return HTTPResponse(respuesta)

def eliminarPedido(request, numero_pedido):
    avatar = getavatar(request)
    pedido = Pedidos.objects.get(numero_pedido=numero_pedido)
    pedido.delete()
    miFormulario = formPedidoFormulario()
    Pedido = Pedidos.objects.all()
    return render(request, "MercadoApp/pedidosFormulario.html", {"miFormulario":miFormulario, "Pedidos": Pedido, "avatar":avatar})

def editarPedido(request, numero_pedido):
    avatar = getavatar(request)
    pedido = get_object_or_404(Pedidos,numero_pedido=numero_pedido)#Pedidos.objects.get(numero_pedido= numero_pedido)
    if request.method == "POST" :#validar si es un pedido valido
        miFormulario = formPedidoFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            pedido.numero_pedido = data["numero_pedido"]
            pedido.nombre_producto = data["nombre_producto"]
            pedido.categoria_producto = data["categoria_producto"]
            pedido.cantidad = data["cantidad"]
            pedido.fecha_entrega = data["fecha_entrega"]
            pedido.save()
            #miFormulario = formPedidoFormulario()
            #Pedido = Pedidos.objects.all()
            #return render(request, "MercadoApp/pedidosFormulario.html", {"miFormulario":miFormulario, "Pedidos": Pedido, "avatar":avatar})
            return redirect('Pedidos')
    else:
        miFormulario = formPedidoFormulario(initial={"numero_pedido":pedido.numero_pedido, "nombre_producto": pedido.nombre_producto, "categoria_producto": pedido.categoria_producto, "cantidad":pedido.cantidad, "fecha_entrega": pedido.fecha_entrega})
    return render(request, "MercadoApp/editarPedido.html", {"miFormulario":miFormulario, "pedido":numero_pedido, "avatar":avatar})

#def leerClientes(request):


def loginWeb(request): #ojo no puede llamarse solo login porque ya estoy importantdo una funcion con ese nombre.
    if request.method == "POST":
        user = authenticate(username=request.POST["user"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            #return redirect('inicio')
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
            return redirect('login')
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
    avatar = getavatar(request)
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username=request.user)
            avatar = Avatar(user=user, image= form.cleaned_data["avatar"], id= request.user.id) #el id es parte de nuestra sesion entonces lo tenemos
            avatar.save()
            avatar = Avatar.objects.filter(user=request.user.id) 
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, "MercadoApp/inicio.html", {"avatar": avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            form = AvatarForm()
        except:
            form = AvatarForm()
    return render(request, "MercadoApp/Perfil/avatar.html", {"form": form, "avatar": avatar})
    
def getavatar(request):
    avatar = Avatar.objects.filter(user=request.user.id) #filter, va a buscar algo especifico, va a traer el avatar que le pertenece a ese usuario
    try:
        avatar= avatar[0].image.url # y lo trae como imagen y lo guarda en una variable
    except:
        avatar = None
    return avatar

def add_comment(request):
    Post=Comment.objects.all()
    if request == "POST":
        post = Comment(post=request.POST["post"])
        post.save()
        miFormulario = CommentForm()
        return render(request, "MercadoApp/Productos.html", {"miFormulario":miFormulario, "Post":post})
    else: 
        miFormulario= CommentForm()
    return render(request, "MercadoApp/Productos.html")





#def add_comment(request, nombre):
#    post = get_object_or_404(Productos, nombre= nombre)
#    if request.method == "POST":
#        form = CommentForm(request.POST)
#        if form.is_valid():
#            comment = form.save(commit=False)
#            comment.post = post
#            comment.save()
#            return redirect('Productos', nombre=nombre)
#    else:
#        form = CommentForm()
#    return render(request, 'Productos', {'form': form})

#def getPedidos(request): #OJO! comenté la función Pedidos que está mas arriba
#    pedido = Pedidos.objects.get()
#    if request.method == "POST" :
#        miFormulario = formPedidoFormulario(request.POST)
#        if miFormulario.is_valid:
#            data = miFormulario.cleaned_data
#            pedido.nombre = data["nombre"]
#            pedido.cantidad = data["cantidad"]
#            pedido.fecha = data["fecha entrega"]
#            pedido.save()
#            miFormulario = formPedidoFormulario()
#            Pedido = Pedidos.objects.all()
#            return render(request, "MercadoApp/resumenPedidos.html", {"miFormulario":miFormulario, "Pedidos": Pedido})

#    else:
#        miFormulario = formPedidoFormulario()
#    return render(request, "MercadoApp/Pedidos.html", {"miFormulario":miFormulario})
