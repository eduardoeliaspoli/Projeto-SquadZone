from .models import Categoria,Postagem,Comentario
from django import forms

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome','slug',]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-titulo', 'placeholder':'Ex: Carnes'}),
            'slug': forms.TextInput(attrs={'class': 'form-slug', 'placeholder':'Ex: carne-suina'}),
        }

class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = ['titulo','slug','descricao','categoria','imagem_capa']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-titulo','placeholder': 'Ex: Carne Suína '}),
            'slug': forms.TextInput(attrs={'class':'form-slug','placeholder': 'Ex: carne-suina'}),
            'descricao':forms.Textarea(attrs={'class':'form-descricao','rows':20}),
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']