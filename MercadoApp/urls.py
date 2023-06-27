from django.urls import path, include 
from MercadoApp.views import inicio, Cliente, Productos, Pedidos, clienteFormulario

urlpatterns = [
    path("inicio/", inicio),
    path("Cliente/", Cliente, name="Cliente"),
    path("Productos/", Productos, name="Productos"),
    path("Pedidos/", Pedidos, name="Pedidos"),
    path("clienteFormulario/", clienteFormulario, name="clienteFormulario")
    
]