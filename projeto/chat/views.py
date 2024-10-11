from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pusher
from django.conf import settings
from squadzone.models import Usuario  # Ajuste o nome do modelo se necessário

def chat_view(request):
    usuarios = Usuario.objects.all()
    return render(request, 'chat/chat.html', {'Usuario': Usuario})


# Configurar o Pusher
pusher_client = pusher.Pusher(
    app_id=settings.PUSHER_APP_ID,
    key=settings.PUSHER_KEY,
    secret=settings.PUSHER_SECRET,
    cluster=settings.PUSHER_CLUSTER,
    ssl=True
)

@csrf_exempt
@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        username = request.POST.get('username')  # Captura o nome do usuário
        pusher_client.trigger('chat-channel', 'new-message', {'message': message, 'username': username})
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)

# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Mensagem
import pusher
from django.conf import settings

# Inicializar o Pusher
pusher_client = pusher.Pusher(
    app_id=settings.PUSHER_APP_ID,
    key=settings.PUSHER_KEY,
    secret=settings.PUSHER_SECRET,
    cluster=settings.PUSHER_CLUSTER,
    ssl=True
)

def index(request):
    return render(request, 'chat/index.html')

def enviar_mensagem(request):
    if request.method == 'POST':
        nome_usuario = request.POST.get('nome_usuario')
        mensagem = request.POST.get('mensagem')

        # Salvar a mensagem no banco de dados
        msg = Mensagem(nome_usuario=nome_usuario, mensagem=mensagem)
        msg.save()

        # Enviar mensagem via Pusher
        pusher_client.trigger('chat', 'mensagem', {'nome_usuario': nome_usuario, 'mensagem': mensagem})

        return JsonResponse({'status': 'sucesso'})

def obter_mensagens(request):
    mensagens = Mensagem.objects.all().values('nome_usuario', 'mensagem', 'data_hora')
    return JsonResponse(list(mensagens), safe=False)
