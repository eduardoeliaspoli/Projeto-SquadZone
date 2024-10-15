from django.urls import path,include
from . import views
from agenda import views as agenda_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views




urlpatterns =  [
    path('',views.index, name='index'),   #// PRECISA DO DEF INDEX NAS VIEWS.PY DO SQUADZONE
    path('cadastrar/usuario', views.criarUsuario, name='CriarUsuario'),
    path('cadastrar/time', views.criarTime, name='criarTime'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('agenda/', include('agenda.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
