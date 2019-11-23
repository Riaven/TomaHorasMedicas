from django import forms

class RecuperarCuenta(forms.Form):
    # Para obtener el rut que se desea buscar
    rut = forms.CharField(required= True)