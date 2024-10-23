from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .views import logout_view




urlpatterns =  [
    path('',views.index, name='index'),   #// PRECISA DO DEF INDEX NAS VIEWS.PY DO SQUADZONE
    path('cadastrar/usuario', views.criarUsuario, name='CriarUsuario'),
    path('cadastrar/time', views.criarTime, name='criarTime'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('agenda/', include('agenda.urls')),
    path('Entrar/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

]

