from django.urls import path
<<<<<<< Updated upstream
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send_message/', views.send_message, name='send_message'),
=======
from .views import send_message, chat_view
from .views import send_message # Importando as views


urlpatterns = [
    path('', chat_view, name='chat_view'),  # URL raiz para o chat
    path('send_message/', send_message, name='send_message'),  # URL para enviar mensagens
>>>>>>> Stashed changes
]
