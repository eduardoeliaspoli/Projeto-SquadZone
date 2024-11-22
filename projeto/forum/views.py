from django.shortcuts import render,get_object_or_404, HttpResponse, redirect
from .models import Categoria, Postagem, Comentario, Voto
from .forms import CategoriaForm,PostagemForm,ComentarioForm
from django.contrib.auth.decorators import login_required

def forum(request):
    postagens = Postagem.objects.all()
    
    # Imprime as postagens e seus comentários no terminal para verificar
    for postagem in postagens:
        print(postagem.titulo)
        for comentario in postagem.comentarios.all():
            print(f"  - Comentário: {comentario.texto}")
    
    return render(request, 'forum.html', {'postagens': postagens})

@login_required
def votar_postagem(request, post_id, tipo_voto):
    postagem = Postagem.objects.get(id=post_id)
    
    
    voto_existente = Voto.objects.filter(usuario=request.user, postagem=postagem).first()

    if tipo_voto == 'upvote':
        if voto_existente:
            if voto_existente.tipo_voto == 'upvote':
               
                postagem.upvotes -= 1
                voto_existente.delete()
            else:
               
                postagem.upvotes += 1
                postagem.downvotes -= 1
                voto_existente.tipo_voto = 'upvote'
                voto_existente.save()
        else:
            
            postagem.upvotes += 1
            Voto.objects.create(usuario=request.user, postagem=postagem, tipo_voto='upvote')

    elif tipo_voto == 'downvote':
        if voto_existente:
            if voto_existente.tipo_voto == 'downvote':
                
                postagem.downvotes -= 1
                voto_existente.delete()
            else:
                
                postagem.downvotes += 1
                postagem.upvotes -= 1
                voto_existente.tipo_voto = 'downvote'
                voto_existente.save()
        else:
            
            postagem.downvotes += 1
            Voto.objects.create(usuario=request.user, postagem=postagem, tipo_voto='downvote')

    postagem.save()  

    return redirect('forum')
  



def filtrar_categoria(request,slug_categoria):
    categoria = get_object_or_404(Categoria, slug = slug_categoria)
    postagens = Postagem.objects.filter(categoria=categoria)
    return render(request,"categorias.html",{'postagens':postagens})

@login_required
def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro_sucesso')
    else:
        form = CategoriaForm()
        return render(request,'cadastro.html',{'form':form})

@login_required
def cadastrar_postagem(request):
    if request.method == 'POST':
        form = PostagemForm(request.POST, request.FILES)
        
        if form.is_valid():
            postagem = form.save(commit=False)
            postagem.autor = request.user
            form.save()
            return HttpResponse('Cadastro Efetuado')
        else:
            
            return render(request, 'cadastro.html', {'form': form})
    else:
        form = PostagemForm()
    
    return render(request, 'cadastro.html', {'form': form})

@login_required
def cadastrar_comentario(request, post_id):
    postagem = get_object_or_404(Postagem, id=post_id) 
    form = ComentarioForm(request.POST or None)

    if form.is_valid():
        comentario = form.save(commit=False)
        comentario.usuario = request.user
        comentario.postagem = postagem 
        comentario.save()

        return redirect('forum')  

    return render(request, 'cadastrar_comentario.html', {'form': form, 'postagem': postagem})
    

def cadastro_sucesso(request):
    return HttpResponse('Cadastrado com sucesso')


def filtrar_categoria(request,slug_categoria):
    categoria = get_object_or_404(Categoria, slug = slug_categoria)
    postagens = Postagem.objects.filter(categoria=categoria)
    return render(request,"jogos_categoria.html",{'postagens':postagens})


def ver_postagem(request,slug):
    postagem = get_object_or_404(Postagem,slug = slug)
    comentarios = Comentario.objects.filter(postagem=postagem,ativo=True)
    return render(request,'ver_postagem.html',{'postagem':postagem,'comentarios':comentarios})