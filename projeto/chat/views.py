from django.shortcuts import render
from django.http import JsonResponse
from .models import Message
import pusher
from django.conf import settings


pusher_client = pusher.Pusher(
    app_id=settings.PUSHER_APP_ID,
    key=settings.PUSHER_KEY,
    secret=settings.PUSHER_SECRET,
    cluster=settings.PUSHER_CLUSTER,
    ssl=True
)

def index(request):
    messages = Message.objects.all().order_by('created_at')
    return render(request, 'chat/index.html', {'messages': messages})


def send_message(request):
    if request.method == 'POST' and request.user.is_authenticated:
        message_content = request.POST.get('message')
        
        # Salvar a mensagem no arquivo
        message = Message.objects.create(content=message_content, user=request.user)


        pusher_client.trigger('chat', 'message', {
            'message': message.content,
            'username': message.user.username 
        })

        return JsonResponse({'status': 'Message sent'})
    
    return JsonResponse({'status': 'Invalid request'}, status=400)
