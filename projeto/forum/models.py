from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(max_length=25, unique=True)
    descricao = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'Categoria'
        
    def __str__(self):
        return self.nome

class Postagem(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    descricao = models.TextField()
    criado_em = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    atualizado_em = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem_capa = models.ImageField(upload_to='imagens_capa/', blank=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = 'Postagens'
        
    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE,related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    email = models.EmailField()
    texto = models.TextField(max_length=280)
    criado_em = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)  
    
    class Meta:
        verbose_name_plural = 'Comentarios'
    
    def __str__(self):
        return f'Post:{self.postagem}, {self.usuario.username}'


class Voto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    tipo_voto = models.CharField(max_length=10)

    class Meta:
        unique_together = ('usuario', 'postagem')  

    def __str__(self):
        return f'{self.usuario.username} - {self.tipo_voto} na postagem {self.postagem.titulo}'