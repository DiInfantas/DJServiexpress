from datetime import timezone
from django.db import models

# Create your models here.

#Modelo para el usuario

class Usuario (models.Model):
    nom_usuario = models.CharField(max_length=40, unique=True, primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=40)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)

    def __str__(self):
        return self.nom_usuario

class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True, unique=True)
    nombre_servicio = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre_servicio
    

#Modelo para las horas tomadas

class HorasTomadas(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    vehiculo = models.CharField(max_length=40)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.hora} - {self.vehiculo.patente} - {self.servicio.nombre_servicio}'


