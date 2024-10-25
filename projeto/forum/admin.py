from django.contrib import admin
from .models import Categoria, Comentario, Postagem

class Postagemadmin(admin.ModelAdmin):
    list_display = ('titulo','criado_em','autor','categoria')
    list_display_links = ('titulo','criado_em','autor','categoria')
    list_filter = ('categoria','criado_em')
    date_hierarchy = 'criado_em'

    fieldsets = (
        ('Cabeçalho', {'fields':('titulo','criado_em','autor')}),
        ('Complementares',{'fields':('slug','descricao','imagem_capa','categoria')})
    )

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('postagem', 'nome', 'email', 'criado_em', 'ativo')
    list_display_links = ('postagem', 'nome', 'email', 'criado_em', 'ativo')
    list_filter = ('postagem', 'criado_em', 'ativo')

class Categoriaadmin(admin.ModelAdmin):
    list_display = ('nome','descricao')
    list_display_links = ('nome','descricao')
    list_filter = ('nome',)


#class Comentarioadmin(admin.ModelAdmin):
#    list_display = ('postagem','criado_em','autor','ativo')
#    list_display_links = ('titulo','criado_em','autor','categoria')
#    list_filter = ('categoria','criado_em')
#    date_hierarchy = 'criado_em'

admin.site.register(Categoria,Categoriaadmin)
admin.site.register(Comentario,ComentarioAdmin)
admin.site.register(Postagem,Postagemadmin)

