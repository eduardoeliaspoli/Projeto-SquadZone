from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from .models import Evento
from .forms import adicionarEvento

def agenda(request):
    return render(request, 'agenda.html')

def adicionar_evento(request):
    if request.method == 'POST':
        form= adicionarEvento(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Evento Adicionado!')
        
    else:
        form = adicionarEvento()
    return render(request, 'adicionar_evento.html',{'form':form})

def eventos_json(request):
    eventos = Evento.objects.all().values('id', 'titulo', 'inicio', 'fim')
    return JsonResponse(list(eventos), safe=False)


