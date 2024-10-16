from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(max_length=2500, null = True)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()

    def __str__(self):
        return self.titulo