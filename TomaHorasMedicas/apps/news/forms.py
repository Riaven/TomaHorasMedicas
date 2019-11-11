#Para poder realizar el formulario
from django import forms
#Para importar el modelo con los datos de noticias
from apps.news.models import Noticias


class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticias
        #Lista de campos para el formulario
        fields = [
            'titulo',
            'contenido',
            'fechaPublicacion',
        ]
        # Campos que se mostraran en el formulario
        labels = {
            'titulo' : 'Título',
            'contenido' : 'Contenido',
            'fechaPublicacion' : 'Fecha de publicación',

        }
        #forma en que se pintan en el html
        widgets = {
            'titulo' :forms.TextInput(attrs={'class':'input-field'}),
            'contenido' : forms.TextInput(attrs={'class':'input-field'}),
            'fechaPublicacion' : forms.TextInput(attrs={'class':'datepicker'}),
        }