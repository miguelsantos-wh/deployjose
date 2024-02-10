from django import forms
from personas.models import Persona


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona

        fields = [
            'nombre',
            'sexo',
        ]
        labels = {
            'nombre': 'Nombre',
            'sexo': 'Sexo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
            'sexo': forms.TextInput(attrs = {'class': 'form-control'}),
        }