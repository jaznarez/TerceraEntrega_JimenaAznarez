from django.urls import path, include 
from MercadoApp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/", inicio),
    path("cliente/", cliente, name="Cliente"),
    path("Productos/", Productos, name="Productos"),
    path("Pedidos/", pedidos, name="Pedidos"),
    path("clienteFormulario/", clienteFormulario, name="clienteFormulario"),
    path("getCliente/", getCliente, name="getCliente"),
    path("buscarCliente/", buscarCliente, name="buscarCliente"),
    path("login/", loginWeb, name="login"),
    path("registro/", registro, name="registro"),
    path("Logout/", LogoutView.as_view(template_name = "MercadoApp/login.html"), name="Logout"),
    path("Perfil/", perfilview, name="perfil"),
    path("Perfil/editarPerfil/", editarPerfil, name="editarPerfil"),
    path("Perfil/changePassword/", changePassword, name="changePassword"),
    path("eliminarCliente/<nombre_cliente>", eliminarCliente, name="eliminarCliente"),
    path("editarCliente/<nombre_cliente>", editarCliente, name="editarCliente"),
    path("Perfil/changeAvatar/", editAvatar, name="editAvatar"),
    path("pedidosFormulario/", pedidosFormulario, name="pedidosFormulario"),
    path("eliminarPedido/<numero_pedido>", eliminarPedido, name="eliminarPedido"),
    path("editarPedido/<numero_pedido>", editarPedido, name="editarPedido"),
    path("getPedido/", getPedido, name="getPedido"),
    path("buscarPedido/", buscarPedido, name="buscarPedido"),
]
