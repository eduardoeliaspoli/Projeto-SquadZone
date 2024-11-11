from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    localizacao = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    nivel_reputacao = models.IntegerField(default=3)  
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if self.senha:
            self.senha = make_password(self.senha)  # Criptografa a senha
        super().save(*args, **kwargs)

    def verificar_senha(self, senha):
        return check_password(senha, self.senha) 


class Jogo(models.Model):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class PerfilJogo(models.Model):
    MODALIDADE_CHOICES = [
        ('casual', 'Casual'),
        ('competitivo', 'Competitivo'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='perfis')
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE, related_name='perfis')
    tag = models.CharField(max_length=50, choices=MODALIDADE_CHOICES)
    foto_perfil = models.ImageField(upload_to='imagens_perfil/', blank=True)

    def __str__(self):
        return f'{self.usuario} - {self.jogo}'


class Time(models.Model):
    TAG_CHOICES = [
        ('Casual', 'Casual'),
        ('Competitivo', 'Competitivo'),
    ]

    nome = models.CharField(max_length=255)
    tag = models.CharField(max_length=50, choices=TAG_CHOICES)
    escudo = models.ImageField(upload_to='escudos/')
    criador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='times_criados')

    def __str__(self):
        return self.nome


class JogadorTime(models.Model):
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='jogadores')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='jogadores_times')
    funcao = models.CharField(max_length=255)
    data_entrada = models.DateField()
    data_saida = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.usuario} - {self.time}'


class Forum(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='posts')
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Mentoria(models.Model):
    usuario_experiente = models.ForeignKey(Usuario, related_name='mentorias_experientes', on_delete=models.CASCADE)
    usuario_novato = models.ForeignKey(Usuario, related_name='mentorias_novatos', on_delete=models.CASCADE)
    tema = models.CharField(max_length=255)
    data_mentoria = models.DateField()

    def __str__(self):
        return f'Mentoria de {self.usuario_experiente} para {self.usuario_novato}'


class Treino(models.Model):
    time_1 = models.ForeignKey(Time, related_name='treinos_time_1', on_delete=models.CASCADE)
    time_2 = models.ForeignKey(Time, related_name='treinos_time_2', on_delete=models.CASCADE)
    data_treino = models.DateField()
    hora = models.TimeField()
    agenda = models.ForeignKey('Agenda', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Treino entre {self.time_1} e {self.time_2}'


class Chat(models.Model):
    usuario_enviou = models.ForeignKey(Usuario, related_name='chats_enviados', on_delete=models.CASCADE)
    usuario_recebeu = models.ForeignKey(Usuario, related_name='chats_recebidos', on_delete=models.CASCADE)
    data_envio = models.DateTimeField(auto_now_add=True)
    data_recebido = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Chat de {self.usuario_enviou} para {self.usuario_recebeu}'


class Agenda(models.Model):
    data_atual = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f'Agenda para {self.data_atual} às {self.hora}'


class Amizade(models.Model):
    TAG_CHOICES = [
        ('Ativo', 'Ativo'),
        ('Pendente', 'Pendente'),
        ('Bloqueio', 'Bloqueio')
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='amizades_1')
    amigo = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='amizades_2')
    status = models.CharField(max_length=50, choices=TAG_CHOICES)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['usuario', 'amigo'], name='amizade_unica')
        ]

    

    def save(self, *args, **kwargs):
        if self.usuario.id > self.amigo.id:
            self.usuario, self.amigo = self.amigo, self.usuario
        super().save(*args, **kwargs)