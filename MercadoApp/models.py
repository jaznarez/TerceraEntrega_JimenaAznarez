from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField()
    edad = models.IntegerField()
    def __str__(self):
        return(f"nombre: {self.nombre} - apellido: {self.apellido} - email: {self.email} - telefono: {self.telefono} - edad: {self.edad}")

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

class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #SubCarpeta de avatares
    image = models.ImageField(upload_to="avatares", null= True, blank=True)