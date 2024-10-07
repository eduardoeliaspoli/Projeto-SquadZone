from .models import Usuario, Jogo, PerfilJogo, Time, JogadorTime, Forum, Mentoria, Treino, Chat, Agenda
from django import forms

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'localizacao', 'data_nascimento', 'email', 'verEmail',  'verSenha', 'senha', 'verSenha']
        widgets = {
            'senha': forms.PasswordInput(),
        }
    
class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['nome','tipo',]

class PerfilJogoForms(forms.ModelForm):
    class Meta:
        model = PerfilJogo
        fields = ['usuario','jogo','tag']

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
        fields = ['time_1','time_2', 'data_treino','hora','agenda']
        
class ChatForms(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['usuario_enviou', 'usuario_recebeu']

class AgendaForms(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['data_atual', 'hora']