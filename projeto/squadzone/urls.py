from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import logout_view

urlpatterns = [
    path('', views.index, name='index'),   # PRECISA DO DEF INDEX NAS VIEWS.PY DO SQUADZONE
    path('cadastrar/time', views.criarTime, name='criarTime'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('agenda/', include('agenda.urls')),
    path('Entrar/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('solicitar-amizade/<int:amigo_id>/', views.enviar_solicitacao_amizade, name='solicitar_amizade'),
    path('aceitar-amizade/<int:amigo_id>/', views.aceitar_solicitacao_amizade, name='aceitar_amizade'),
    path('recusar-amizade/<int:amigo_id>/', views.recusar_solicitacao_amizade, name='recusar_amizade'),
    path('amigos/', views.lista_amigos, name='lista_amigos'),  
    path('usuarios/',views.lista_usuarios, name= 'lista_usuarios' ),
    path('solicitacoes-pendentes/', views.solicitacoes_pendentes, name='solicitacoes_pendentes'),
    path('perfil/<str:username>/', views.perfil_usuario, name='perfil_usuario'),
    path('criar-perfil/', views.criar_perfil, name='criar_perfil'),
    path('chat/<int:user_id>/', views.private_chat, name='private_chat'),
]