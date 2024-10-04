from django.contrib import admin
from .models import Usuario, Jogo, PerfilJogo, Time, JogadorTime, Forum, Mentoria, Treino, Chat, Agenda

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_criacao')  # Remova 'nivel_reputacao'
    search_fields = ('nome', 'email')

    def save_model(self, request, obj, form, change):
        if not change:  # Se for uma criação
            obj.nivel_reputacao = 3  # Define o valor padrão aqui
        super().save_model(request, obj, form, change)


@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo')
    search_fields = ('nome',)

@admin.register(PerfilJogo)
class PerfilJogoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'jogo', 'tag')

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
