from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=255)
    inicio = models.DateTimeField(null=True)
    fim = models.DateTimeField(null=True)

    def __str__(self):
        return self.titulo