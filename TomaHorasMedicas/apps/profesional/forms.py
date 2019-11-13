from django import forms
from .models import Profesional

class ProfesionalForm (forms.ModelForm):
    class Meta():
        model = Profesional
        fields = [
            'nombre',
            'sector',
            'horarioAtencion',
            'foto',
            'areaAtencion',
        ]
        labels = {
            'nombre' : 'Nombre',
            'sector' : 'Sector',
            'horarioAtencion' : 'Horario de Atención',
            'foto' : 'CARGAR FOTO',
            'areaAtencion' : 'Área de atención',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class' : 'input-field'}),
            'sector' : forms.Select(attrs={'class' : 'select'}),
            'horarioAtencion' : forms.TextInput(attrs={'class' : 'input-field'}),
            #'foto' : forms.ImageField(), <-- la foto no debe de llebar attrs
            'areaAtencion' : forms.Select(attrs={'class' : 'select'}),
        }