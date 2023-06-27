from django.urls import path, include 
from MercadoApp.views import inicio, Cliente, Productos, Pedidos, clienteFormulario, getCliente, buscarCliente

urlpatterns = [
    path("inicio/", inicio),
    path("Cliente/", Cliente, name="Cliente"),
    path("Productos/", Productos, name="Productos"),
    path("Pedidos/", Pedidos, name="Pedidos"),
    path("clienteFormulario/", clienteFormulario, name="clienteFormulario"),
    path("getCliente/", getCliente, name="getCliente"),
    path("buscarCliente/", buscarCliente, name="buscarCliente"),

]
