from django.db import models
from django.contrib.auth.models import User

class PerfilJogo(models.Model):
    MODALIDADE_CHOICES = [
        ('casual', 'Casual'),
        ('competitivo', 'Competitivo'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    jogos = models.ManyToManyField('Jogo', related_name='jogadores')
    tipo_jogador = models.CharField(max_length=50, choices=MODALIDADE_CHOICES)
    data_nascimento = models.DateField()
    localizacao = models.CharField(max_length=255)
    foto_perfil = models.ImageField(upload_to='imagens_perfil/', blank=True)

    def __str__(self):
        return f'Perfil de {self.usuario.username}'

class Jogo(models.Model):
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Time(models.Model):
    TAG_CHOICES = [
        ('Casual', 'Casual'),
        ('Competitivo', 'Competitivo'),
    ]

    nome = models.CharField(max_length=255)
    tag = models.CharField(max_length=50, choices=TAG_CHOICES)
    escudo = models.ImageField(upload_to='escudos/')
    criador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='times_criados')

    def __str__(self):
        return self.nome

class JogadorTime(models.Model):
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='jogadores')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jogadores_times')
    funcao = models.CharField(max_length=255)
    data_entrada = models.DateField()
    data_saida = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.time.nome}'

class Forum(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Mentoria(models.Model):
    usuario_experiente = models.ForeignKey(User, related_name='mentorias_experientes', on_delete=models.CASCADE)
    usuario_novato = models.ForeignKey(User, related_name='mentorias_novatos', on_delete=models.CASCADE)
    tema = models.CharField(max_length=255)
    data_mentoria = models.DateField()

    def __str__(self):
        return f'Mentoria de {self.usuario_experiente.username} para {self.usuario_novato.username}'

class Treino(models.Model):
    time_1 = models.ForeignKey(Time, related_name='treinos_time_1', on_delete=models.CASCADE)
    time_2 = models.ForeignKey(Time, related_name='treinos_time_2', on_delete=models.CASCADE)
    data_treino = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f'Treino entre {self.time_1.nome} e {self.time_2.nome}'

class Chat(models.Model):
    usuario_enviou = models.ForeignKey(User, related_name='chats_enviados', on_delete=models.CASCADE)
    usuario_recebeu = models.ForeignKey(User, related_name='chats_recebidos', on_delete=models.CASCADE)
    data_envio = models.DateTimeField(auto_now_add=True)
    data_recebido = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Chat de {self.usuario_enviou.username} para {self.usuario_recebeu.username}'

class Agenda(models.Model):
    data_atual = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f'Agenda para {self.data_atual} às {self.hora}'

class Amizade(models.Model):
    PENDENTE = 'Pendente'
    ACEITO = 'Aceito'
    RECUSADO = 'Recusado'

    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (ACEITO, 'Aceito'),
        (RECUSADO, 'Recusado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacoes_enviadas')
    amigo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacoes_recebidas')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDENTE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} - {self.amigo.username} ({self.status})'

    class Meta:
        unique_together = ('usuario', 'amigo')

class Notificacao(models.Model):
    TIPO_CHOICES = [
        ('amizade', 'Pedido de amizade'),
        ('mensagem', 'Mensagem'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificacoes')
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    conteudo = models.TextField()
    lida = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificação para {self.usuario.username}: {self.conteudo[:30]}"
