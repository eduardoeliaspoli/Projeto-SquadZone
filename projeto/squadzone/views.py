from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from .forms import TimeForms, TreinoForms,AmizadeForm,PerfilJogoForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages
from .models import Message
from .models import Amizade,PerfilJogo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from . import models
from django.db.models import Q
 
 


def index(request):
    return render(request, 'index.html')

def buscar(request):
    usuarios = User.objects.all()  # Busca todos os usuários cadastrados
    return render(request, 'buscar.html', {'usuarios': usuarios})


def criar_perfil(request):
    if request.method == 'POST':
        form = PerfilJogoForm(request.POST, request.FILES)
        if form.is_valid():
            perfil = form.save(commit=False)
            perfil.usuario = request.user
            perfil.save()
            return redirect('perfil_view')
    else:
        form = PerfilJogoForm()
    return render(request, 'criar_perfil.html', {'form': form})

def criarTime(request):
    if request.method == 'POST':
        form = TimeForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
        else:
            print(form.errors)
    else:
        form = TimeForms()
       
    return render(request, 'criarTime.html', {'form': form})
 

 
def agenda(request):
    return render(request, 'agenda.html')
 
 
def sucesso(request):
 
    return HttpResponse('Cadastrado com sucesso')
 
def treinos(request):
    if request.method == 'POST':
        form = TreinoForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
        else:
            print(form.errors)
    else:
        form = TreinoForms()
       
    return render(request, 'novoTreino.html', {'form': form})
 
def login_view(request):
    return LoginView.as_view(template_name='login.html')(request)
 
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def enviar_solicitacao_amizade(request, amigo_id):
    amigo = User.objects.get(id=amigo_id)
    
    if amigo == request.user:
        messages.error(request, "Você não pode adicionar a si mesmo como amigo.")
        return redirect('lista_usuarios')

    if Amizade.objects.filter(usuario=request.user, amigo=amigo, status=Amizade.PENDENTE).exists():
        messages.error(request, "Você já enviou um pedido de amizade para esse usuário.")
        return redirect('lista_usuarios')
    

    if Amizade.objects.filter(usuario=request.user, amigo=amigo, status=Amizade.ACEITO).exists() or \
       Amizade.objects.filter(usuario=amigo, amigo=request.user, status=Amizade.ACEITO).exists():
        messages.error(request, "Você já é amigo dessa pessoa.")
        return redirect('lista_usuarios')
    

    Amizade.objects.create(usuario=request.user, amigo=amigo, status=Amizade.PENDENTE)
    messages.success(request, "Pedido de amizade enviado com sucesso!")
    return redirect('lista_usuarios')

@login_required
def aceitar_solicitacao_amizade(request, amigo_id):
    # Encontra a solicitação de amizade específica e a marca como aceita
    amizade = Amizade.objects.get(usuario=amigo_id, amigo=request.user, status=Amizade.PENDENTE)
    amizade.status = Amizade.ACEITO
    amizade.save()

    Amizade.objects.filter(
        usuario=request.user, amigo=amigo_id, status=Amizade.PENDENTE
    ).delete()

    messages.success(request, "Pedido de amizade aceito!")
    return redirect('lista_usuarios')


def perfil_usuario(request, username):
    perfil = get_object_or_404(PerfilJogo, usuario__username=username)
    
    context = {
        'perfil': perfil
    }
    return render(request, 'perfil_usuario.html', context)

@login_required
def recusar_solicitacao_amizade(request, amigo_id):
    amizade = Amizade.objects.get(usuario=amigo_id, amigo=request.user, status=Amizade.PENDENTE)
    amizade.status = Amizade.RECUSADO
    amizade.save()
    messages.success(request, "Pedido de amizade recusado!")
    return redirect('lista_usuarios')

def lista_amigos(request):
    
    amigos_ativos = Amizade.objects.filter(usuario=request.user, status=Amizade.ACEITO) | \
                    Amizade.objects.filter(amigo=request.user, status=Amizade.ACEITO)
                    

    amigos = [amizade.amigo for amizade in amigos_ativos] + [amizade.usuario for amizade in amigos_ativos]
    
    amigos = list(set(amigos) - {request.user})
    
    return render(request, 'lista_amigos.html', {'amigos': amigos})


def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

@login_required
def solicitacoes_pendentes(request):
    solicitacoes = Amizade.objects.filter(amigo=request.user, status=Amizade.PENDENTE)
    return render(request, 'solicitacoes_pendentes.html', {'solicitacoes': solicitacoes})


@login_required
def private_chat(request, user_id):
    other_user = get_object_or_404(User, id=user_id)

    # Histórico de mensagens entre os dois usuários
    messages = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver=other_user)) |
        (Q(sender=other_user) & Q(receiver=request.user))
    )

    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Message.objects.create(sender=request.user, receiver=other_user, content=content)

            return JsonResponse({'status': 'Mensagem enviada com sucesso!'})

    return render(request, 'chat/private_chat.html', {'messages': messages, 'other_user': other_user})
