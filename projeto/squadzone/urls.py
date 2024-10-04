from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings



urlpatterns =  [
    path('',views.index, name='index'),   #// PRECISA DO DEF INDEX NAS VIEWS.PY DO SQUADZONE
    path('cadastrar/usuario', views.criarUsuario, name='CriarUsuario'),
    path('cadastrar/time', views.criarTime, name='criarTime'),
    path('sucesso/', views.sucesso, name='sucesso'),

]