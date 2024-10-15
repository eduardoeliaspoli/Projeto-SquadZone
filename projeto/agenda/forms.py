from django import forms
from .models import Evento

class adicionarEvento(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo','inicio','fim'] 