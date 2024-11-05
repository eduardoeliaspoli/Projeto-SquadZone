from django.shortcuts import render,get_object_or_404, HttpResponse, redirect
from .models import Categoria, Postagem, Comentario, Voto
from .forms import CategoriaForm,PostagemForm,ComentarioForm
from django.contrib.auth.decorators import login_required

def forum(request):
    postagens = Postagem.objects.all()
    return render(request, 'forum.html', {'postagens': postagens})

@login_required
def votar_postagem(request, post_id, tipo_voto):
    postagem = Postagem.objects.get(id=post_id)
    
    # Verifica se o usuário já votou nesta postagem
    voto_existente = Voto.objects.filter(usuario=request.user, postagem=postagem).first()

    if tipo_voto == 'upvote':
        if voto_existente:
            if voto_existente.tipo_voto == 'upvote':
                # Se já votou para cima, remove o voto
                postagem.upvotes -= 1
                voto_existente.delete()
            else:
                # Se votou para baixo, troca para cima
                postagem.upvotes += 1
                postagem.downvotes -= 1
                voto_existente.tipo_voto = 'upvote'
                voto_existente.save()
        else:
            # Novo voto
            postagem.upvotes += 1
            Voto.objects.create(usuario=request.user, postagem=postagem, tipo_voto='upvote')

    elif tipo_voto == 'downvote':
        if voto_existente:
            if voto_existente.tipo_voto == 'downvote':
                # Se já votou para baixo, remove o voto
                postagem.downvotes -= 1
                voto_existente.delete()
            else:
                # Se votou para cima, troca para baixo
                postagem.downvotes += 1
                postagem.upvotes -= 1
                voto_existente.tipo_voto = 'downvote'
                voto_existente.save()
        else:
            # Novo voto
            postagem.downvotes += 1
            Voto.objects.create(usuario=request.user, postagem=postagem, tipo_voto='downvote')

    postagem.save()  # Salva as alterações na postagem

    return redirect('forum')  # Retorne para a página do fórum
  # Redireciona para a página do fórum



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
