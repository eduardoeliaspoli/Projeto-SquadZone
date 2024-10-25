from .models import Categoria,Postagem,Comentario
from django import forms

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome','slug','descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-titulo', 'placeholder':'Ex: Carnes'}),
            'slug': forms.TextInput(attrs={'class': 'form-slug', 'placeholder':'Ex: carne-suina'}),
            'descricao': forms.Textarea(attrs={'class': 'form-descricao', 'rows':10})
        }

class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = ['titulo','slug','descricao','categoria','autor','imagem_capa']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-titulo','placeholder': 'Ex: Carne Suína '}),
            'slug': forms.TextInput(attrs={'class':'form-slug','placeholder': 'Ex: carne-suina'}),
            'descricao':forms.Textarea(attrs={'class':'form-descricao','rows':20})
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['postagem','nome','email','texto']
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-nome-usuario','placeholder': 'Ex: Pablo Scarelli'}),
            'email': forms.TextInput(attrs={'class':'form-slug','placeholder': 'Ex: dudu123@gmail.com'}),
            'texto': forms.Textarea(attrs={'class':'form-descricao','rows':5})
        } 