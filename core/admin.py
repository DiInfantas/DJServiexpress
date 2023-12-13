from django.contrib import admin
from .models import Cita, Vehiculo, Cliente, Trabajador
# Register your models here.

admin.site.register(Cita)
admin.site.register(Vehiculo)
admin.site.register(Cliente)
admin.site.register(Trabajador)