from django.shortcuts import render, redirect, HttpResponse
from .forms import UsuarioForm, TimeForms,TreinoForms


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

#class TreinoForms(forms.ModelForm):
    #class Meta:
     #   model = Treino
      #  fields = ['time_1','time_2', 'data_treino','hora','agenda']

