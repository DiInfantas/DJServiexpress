from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import VehiculoForm, CitaForm
from .models import Vehiculo, Cita
# Create your views here.

#login y registro

#registro de usuarios




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('ingresar_vehiculo')  # Redirige a la vista de ingresar vehículo
    else:
        form = UserCreationForm()
        
    return render(request, 'core/Registro.html', {'form': form})

#login de usuarios












def ingresar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)
            vehiculo.cliente = request.user.cliente  # Asigna el cliente al vehículo
            vehiculo.save()
            return redirect('dashboard')  # Redirige a tu vista de dashboard
    else:
        form = VehiculoForm()
    return render(request, 'ingresar_vehiculo.html', {'form': form})





def index (request):
    return render(request, "core/index.html")

def login (request):
    return render(request, "core/Login.html")

def registro (request):
    return render(request, "core/Registro.html")

def rePass (request):
    return render(request, "core/rePass.html")

def tomadehoras (request):
    
    data = {
        'form': CitaForm(),
    }
    if request.method == 'POST':
        formulario = CitaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Formulario enviado correctamente"
        else:
            data['form'] = formulario
            print(formulario.errors)
    
    
    return render(request, "core/tomadehoras.html", data)

def horastomadas (request):
    citas = Cita.objects.all()
    data = {
        'Citas': citas
    }
    return render(request, "core/horastomadas.html", data)
def editarhora (request):
    return render(request, "core/editarhora.html")