from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True )
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Adicione este campo

    class Meta:
        ordering = ['created_at']  # Ordenação em ordem crescente (ASC)
        
    def __str__(self):
        return f"{self.user.username}: {self.content}"  # Alterado para incluir o nome do usuário

