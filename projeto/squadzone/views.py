from django.shortcuts import render, redirect, HttpResponse
from .forms import UsuarioForm, TimeForms


def index(request):
    return render(request, 'index.html')

#def index(request):
#    postagens = Postagem.objects.all()3
#     return render(request, 'index.html', {'postagens': postagens})

#
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

