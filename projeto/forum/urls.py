from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.forum, name='forum'),
    path('cadastrar/comentario',views.cadastrar_comentario, name='cadastrar_postagem'),
    path('cadastrar/postagem',views.cadastrar_postagem, name='cadastro'),
    path('cadastrar/categoria',views.cadastrar_categoria, name='cadastrar_categoria'),
    path('categoria/<slug:slug_categoria>/', views.filtrar_categoria,name='filtrar_categoria'),
    path('votar/<int:post_id>/<str:tipo_voto>/', views.votar_postagem, name='votar_postagem'),
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)