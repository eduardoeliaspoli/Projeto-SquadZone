from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from .forms import UsuarioForm, TimeForms, TreinoForms,AmizadeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages
from .models import Amizade,Usuario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
 
 
def index(request):
    return render(request, 'index.html')
 
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
 
 
 
def criarUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.nivel_reputacao = 3
            usuario.save()
            return redirect('sucesso')
    else:
        form = UsuarioForm()  # Inicializa o formulário para requisições GET
       
    return render(request, 'CriarUsuario.html', {'form': form})
 
 
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

    # Verifica se já existe um pedido pendente de amizade
    if Amizade.objects.filter(usuario=request.user, amigo=amigo, status=Amizade.PENDENTE).exists():
        messages.error(request, "Você já enviou um pedido de amizade para esse usuário.")
        return redirect('lista_usuarios')
    
    # Verifica se já existe uma amizade ativa
    if Amizade.objects.filter(usuario=request.user, amigo=amigo, status=Amizade.ACEITO).exists() or \
       Amizade.objects.filter(usuario=amigo, amigo=request.user, status=Amizade.ACEITO).exists():
        messages.error(request, "Você já é amigo dessa pessoa.")
        return redirect('lista_usuarios')
    
    # Cria um novo pedido de amizade
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

@login_required
def recusar_solicitacao_amizade(request, amigo_id):
    amizade = Amizade.objects.get(usuario=amigo_id, amigo=request.user, status=Amizade.PENDENTE)
    amizade.status = Amizade.RECUSADO
    amizade.save()
    messages.success(request, "Pedido de amizade recusado!")
    return redirect('lista_usuarios')

def lista_amigos(request):
    # Obtém as amizades ativas onde o usuário é o remetente ou o destinatário
    amigos_ativos = Amizade.objects.filter(usuario=request.user, status=Amizade.ACEITO) | \
                    Amizade.objects.filter(amigo=request.user, status=Amizade.ACEITO)
                    
    # Cria uma lista dos usuários amigos, considerando o remetente e o destinatário
    amigos = [amizade.amigo for amizade in amigos_ativos] + [amizade.usuario for amizade in amigos_ativos]
    
    # Remove duplicados
    amigos = list(set(amigos) - {request.user})
    
    return render(request, 'lista_amigos.html', {'amigos': amigos})


def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'lista_usuarios.html', {'usuarios': usuarios})

@login_required
def solicitacoes_pendentes(request):
    solicitacoes = Amizade.objects.filter(amigo=request.user, status=Amizade.PENDENTE)
    return render(request, 'solicitacoes_pendentes.html', {'solicitacoes': solicitacoes})
