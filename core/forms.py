from django import forms 
from .models import Vehiculo, Cita

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'placa', 'cliente']

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'
        
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),	
            'hora': forms.TimeInput(attrs={'type': 'time'})
        }
        

