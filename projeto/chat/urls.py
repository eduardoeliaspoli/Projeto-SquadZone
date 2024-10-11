from django.urls import path
from .views import send_message, chat_view  # Importando as views
from .views import index, enviar_mensagem, obter_mensagens

urlpatterns = [
    path('', chat_view, name='chat_view'),  # URL raiz para o chat
    path('send-message/', send_message, name='send_message'),  # URL para enviar mensagens
    path('mensagens/', obter_mensagens, name='obter_mensagens'),
]
