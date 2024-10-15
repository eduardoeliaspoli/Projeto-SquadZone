from django.contrib import admin
from .models import Evento

# Register your models here.
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'inicio','fim')  # Remova 'nivel_reputacao'