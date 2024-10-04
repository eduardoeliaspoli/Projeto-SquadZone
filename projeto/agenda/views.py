from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Evento
from django.utils import timezone

# Create your views here.
def agenda(request):
    return render(request, 'agenda.html')

# views.py

def eventos_json(request):
    eventos = Evento.objects.all()
    eventos_list = []
    for evento in eventos:
        eventos_list.append({
            'title': evento.titulo,
            'start': evento.inicio.strftime("%Y-%m-%dT%H:%M:%S"),
            'end': evento.fim.strftime("%Y-%m-%dT%H:%M:%S") if evento.fim else None,
        })
    return JsonResponse(eventos_list, safe=False)


def adicionar_evento(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        inicio = request.POST.get('inicio')
        fim = request.POST.get('fim')
        evento = Evento(titulo=titulo, descricao=descricao, inicio=inicio, fim=fim)
        evento.save()

        return redirect('eventos_listar')  # Redireciona para uma página que lista os eventos, por exemplo
    return render(request, 'adicionar_evento.html')