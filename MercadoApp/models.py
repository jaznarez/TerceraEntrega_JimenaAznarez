from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()
    edad = models.IntegerField()

class Productos(models.Model):
    categoria = models.IntegerField()
    nombre = models.CharField(max_length=30)
    tipo = models.IntegerField()

class Pedidos(models.Model):
    cliente = Cliente #se puede llamar a una clase??
    producto = Productos
    fecha = models.DateField()
    preparado = models.BooleanField()
    entregado = models.BooleanField()
    