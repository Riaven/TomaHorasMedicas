from django import forms
from apps.paciente.models import Paciente

class PacienteForm(froms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombre',
            'apellido',
            'fechaNacimiento',
            'direccion',
            'telefono',
            'estadoCivil',
            'numeroHijos',
            'problemasSalud',
            'peso',
            'altura',
        ]
        labels ={
            'nombre' : 'Nombre',
            'apellido' :'Apellidos',
            'fechaNacimiento' : 'Fecha de Nacimiento',
            'direccion' : 'Dirección',
            'telefono' : 'Teléfono',
            'estadoCivil' : 'Estado Civil',
            'numeroHijos' : 'Número de hijos',
            'problemasSalud' : 'Problemas de salud',
            'peso' : 'Peso',
            'altura' : 'Altura',
        }
        