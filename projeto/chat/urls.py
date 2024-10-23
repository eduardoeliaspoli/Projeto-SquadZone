from django.urls import path
from . import views

urlpatterns = [
    path('sala/', views.chat_index, name='chat_index'),
    path('send_message/', views.send_message, name='send_message'),
]  
