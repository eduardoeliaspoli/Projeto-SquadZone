from django.shortcuts import render
from django.http import JsonResponse
<<<<<<< Updated upstream
from .models import Message
import pusher
from django.conf import settings
=======
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from squadzone.models import Usuario
import pusher




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
>>>>>>> Stashed changes

pusher_client = pusher.Pusher(
    app_id=settings.PUSHER_APP_ID,
    key=settings.PUSHER_KEY,
    secret=settings.PUSHER_SECRET,
    cluster=settings.PUSHER_CLUSTER,
    ssl=True
)

def index(request):
    messages = Message.objects.all().order_by('-created_at')
    return render(request, 'chat/index.html', {'messages': messages})

<<<<<<< Updated upstream
def send_message(request):
    if request.method == 'POST':
        message_content = request.POST.get('message')
        message = Message.objects.create(content=message_content)

        pusher_client.trigger('chat', 'message', {
            'message': message.content
        })

        return JsonResponse({'status': 'Message sent'})
    return JsonResponse({'status': 'Invalid request'}, status=400)
=======
>>>>>>> Stashed changes
