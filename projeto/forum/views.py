from django.shortcuts import render,get_object_or_404, HttpResponse, redirect
from .models import Categoria, Postagem, Comentario
from .forms import CategoriaForm,PostagemForm,ComentarioForm

def forum(request):
    postagens = Postagem.objects.all()
    return render(request, 'forum.html', {'postagens': postagens})


def filtrar_categoria(request,slug_categoria):
    categoria = get_object_or_404(Categoria, slug = slug_categoria)
    postagens = Postagem.objects.filter(categoria=categoria)
    return render(request,"categorias.html",{'postagens':postagens})

def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_sucesso')
    else:
        form = CategoriaForm()
        return render(request,'cadastro.html',{'form':form})

def cadastrar_postagem(request):
    if request.method == 'POST':
        form = PostagemForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponse('Cadastro Efetuado')
        else:
            # Se o formulário não for válido, renderize novamente com os erros
            return render(request, 'cadastro.html', {'form': form})
    else:
        form = PostagemForm()
    
    return render(request, 'cadastro.html', {'form': form})

    
def cadastrar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_sucesso')
    else:
        form = ComentarioForm()
        return render(request,'cadastro.html',{'form':form})
    

def cadastro_sucesso(request):
    return HttpResponse('Cadastrado com sucesso')
