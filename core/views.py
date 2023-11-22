from django.shortcuts import render, redirect


# Create your views here.

def index (request):
    return render(request, "core/index.html")

def login (request):
    return render(request, "core/Login.html")

def registro (request):
    return render(request, "core/Registro.html")

def rePass (request):
    return render(request, "core/rePass.html")

def tomadehoras (request):
    return render(request, "core/tomadehoras.html")

def horastomadas (request):
    return render(request, "core/horastomadas.html")
def editarhora (request):
    return render(request, "core/editarhora.html")