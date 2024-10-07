# agenda/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.agenda,name='agenda'),
    path('adicionar/', views.adicionar_evento, name='adicionar_evento'),
    path('eventos/', views.eventos_json, name='eventos_listar'), 
]