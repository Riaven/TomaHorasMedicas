from django import forms
from apps.paciente.models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'rut',
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
            'rut' : 'RUN',
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
        widgets = {
            'rut' : forms.TextInput(attrs={'class' : 'input-field'}),
            'nombre' : forms.TextInput(attrs={'class' : 'input-field'}),
            'apellido' : forms.TextInput(attrs={'class' : 'input-field'}),
            'fechaNacimiento' : forms.TextInput(attrs={'class':'datepicker'}),
            'direccion' : forms.TextInput(attrs={'class' : 'input-field'}),
            'telefono' : forms.TextInput(attrs={'class' : 'input-field'}),
            'estadoCivil' :forms.Select(attrs={'class' : 'select'}),
            'numeroHijos' : forms.NumberInput(),
            'problemasSalud' : forms.Select(attrs={'class' : 'select'}),
            'peso' : forms.NumberInput(),
            'altura' : forms.NumberInput(),
        }