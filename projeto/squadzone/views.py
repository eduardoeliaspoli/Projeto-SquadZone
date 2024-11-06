from django.shortcuts import render, redirect, HttpResponse
from .forms import UsuarioForm, TimeForms, TreinoForms
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth import login
from .forms import SignUpForm

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário automaticamente após o cadastro
            return redirect("home")  # Redireciona para a página inicial ou outra página
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})








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