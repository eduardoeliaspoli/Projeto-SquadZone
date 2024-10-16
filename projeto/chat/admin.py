from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at')
    ordering = ('created_at',) 

admin.site.register(Message, MessageAdmin)
