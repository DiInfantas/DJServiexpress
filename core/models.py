from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Trabajador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} -Numero de telefono: {self.telefono}"

class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)
    def __str__(self):
        return f"Marca: {self.marca}| Modelo: {self.modelo}| Patente: {self.placa}"

class Cita(models.Model):  # Nueva relación con el modelo User
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    servicio = models.CharField(max_length=200)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.fecha} - {self.hora} - {self.vehiculo} - {self.servicio}"