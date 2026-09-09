from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'estado', 'proyecto']

    def __init__(self, *args, usuario=None, **kwargs):
        super().__init__(*args, **kwargs)
        if usuario:
            # Solo mostrar proyectos que pertenecen al usuario logueado
            self.fields['proyecto'].queryset = self.fields['proyecto'].queryset.filter(usuario=usuario)