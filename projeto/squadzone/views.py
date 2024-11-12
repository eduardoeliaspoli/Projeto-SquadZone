from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from .forms import UsuarioForm, TimeForms, TreinoForms,AmizadeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages
from .models import Amizade
 
 
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


def criar_amizade(request, amigo_id):
    if request.method == 'POST':
        form = AmizadeForm(request.POST)
        amigo = amigo_id  

        if request.user.id == amigo:
            messages.error(request, "Você não pode adicionar a si mesmo como amigo.")
            return redirect('criar_amizade', amigo_id=amigo)


        if Amizade.objects.filter(usuario=request.user, amigo_id=amigo).exists():
            messages.error(request, "Você já tem um pedido de amizade com essa pessoa.")
            return redirect('criar_amizade', amigo_id=amigo)

        if form.is_valid():
            amizade = form.save(commit=False)
            amizade.usuario = request.user
            amizade.amigo_id = amigo
            amizade.save()
            messages.success(request, "Pedido de amizade enviado com sucesso!")
            return redirect('sucesso')
    else:
        form = AmizadeForm()

    return render(request, 'criar_amizade.html', {'form': form, 'amigo_id': amigo_id})


def lista_amigos(request):
    amigos = Amizade.objects.filter(usuario=request.user, status='Ativo') | Amizade.objects.filter(amigo=request.user, status='Ativo')
    return render(request, 'lista_amigos.html', {'amigos': amigos})

