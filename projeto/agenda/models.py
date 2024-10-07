from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)
    inicio = models.DateTimeField()
    fim = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.titulo