from .models import Jogo, PerfilJogo, Time, JogadorTime, Forum, Mentoria, Treino, Chat, Agenda,Amizade
from django import forms
    
class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['nome','tipo',]

class PerfilJogoForm(forms.ModelForm):
    class Meta:
        model = PerfilJogo
        fields = ['jogos', 'tipo_jogador', 'data_nascimento', 'localizacao', 'foto_perfil']
    
    jogos = forms.ModelMultipleChoiceField(queryset=Jogo.objects.all(), widget=forms.CheckboxSelectMultiple)
    tipo_jogador = forms.ChoiceField(choices=PerfilJogo.MODALIDADE_CHOICES)
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class TimeForms(forms.ModelForm):
    class Meta:
        model = Time
        fields = ['nome', 'tag' , 'escudo', 'criador']

class JogadorTimeForms(forms.ModelForm):
    class Meta:
        model = JogadorTime
        fields = ['time','usuario','funcao','data_entrada','data_saida']
        
class ForumForms(forms.ModelForm): 
    class Meta:
        model = Forum
        fields = ['usuario', 'titulo','conteudo']
        
class MentoriaForms(forms.ModelForm):
    class Meta:
        model = Mentoria
        fields = ['usuario_experiente', 'usuario_novato', 'tema', 'data_mentoria']
        
class TreinoForms(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['time_1','time_2', 'data_treino','hora',]
        
class ChatForms(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['usuario_enviou', 'usuario_recebeu']

class AgendaForms(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['data_atual', 'hora']


class AmizadeForm(forms.ModelForm):
    class Meta:
        model = Amizade
        fields = ['status', 'amigo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].initial = 'Pendente' 
        self.fields['status'].widget = forms.HiddenInput()