from django.db import models

# Create your models here.
class Mensagens(models.Model):
    usuarioMensagem = models.CharField(max_length=50)
    mensagem = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuarioMensagem}: {self.mensagem}"
