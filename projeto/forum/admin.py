from django.contrib import admin
from .models import Categoria, Comentario, Postagem, Voto  # Importando o modelo Voto

class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'criado_em', 'autor', 'categoria')
    list_display_links = ('titulo', 'criado_em', 'autor', 'categoria')
    list_filter = ('categoria', 'criado_em')
    date_hierarchy = 'criado_em'

    fieldsets = (
        ('Cabeçalho', {'fields': ('titulo', 'criado_em', 'autor')}),
        ('Complementares', {'fields': ('slug', 'descricao', 'imagem_capa', 'categoria')})
    )

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('postagem', 'usuario', 'criado_em', 'ativo')
    list_display_links = ('postagem', 'usuario', 'criado_em', 'ativo')
    list_filter = ('postagem', 'criado_em', 'ativo')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    list_display_links = ('nome', 'descricao')
    list_filter = ('nome',)

class VotoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'postagem', 'tipo_voto')
    list_display_links = ('usuario', 'postagem')
    list_filter = ('tipo_voto', 'usuario', 'postagem')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Postagem, PostagemAdmin)
admin.site.register(Voto, VotoAdmin)  # Registre o modelo Voto
