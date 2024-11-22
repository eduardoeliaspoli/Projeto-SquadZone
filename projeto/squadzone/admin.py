from django.contrib import admin
from .models import PerfilJogo, Jogo, PerfilJogo, Time, JogadorTime, Forum, Mentoria, Treino, Chat, Agenda,Amizade
@admin.register(PerfilJogo)
class PerfilJogoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'tipo_jogador', 'data_nascimento', 'localizacao']
    search_fields = ['usuario__username', 'tipo_jogador', 'localizacao']

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')
    search_fields = ('nome',)

@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tag', 'criador') 
    search_fields = ('nome',)

@admin.register(JogadorTime)
class JogadorTimeAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'time', 'funcao', 'data_entrada', 'data_saida')  # Atualize os nomes
    search_fields = ('usuario__nome', 'time__nome')

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'titulo', 'data_postagem')  # Atualize os nomes
    search_fields = ('titulo',)

@admin.register(Mentoria)
class MentoriaAdmin(admin.ModelAdmin):
    list_display = ('usuario_experiente', 'usuario_novato', 'tema', 'data_mentoria')  # Atualize os nomes
    search_fields = ('tema',)

@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    list_display = ('time_1', 'time_2', 'data_treino', 'hora')  # Atualize os nomes
    search_fields = ('time_1__nome', 'time_2__nome')

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('usuario_enviou', 'usuario_recebeu', 'data_envio', 'data_recebido')  # Atualize os nomes
    search_fields = ('usuario_enviou__nome', 'usuario_recebeu__nome')

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('data_atual', 'hora')
    search_fields = ('data_atual',)

@admin.register(Amizade)
class AmizadeAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'amigo', 'status', 'data_criacao')  # Exibir os campos relevantes
    search_fields = ('usuario__nome', 'amigo__nome', 'status')  # Permite pesquisa por nome dos usuários e status
    list_filter = ('status',)  # Filtro por status de amizade
    ordering = ('data_criacao',)  # Ordenar as amizades pela data de criação