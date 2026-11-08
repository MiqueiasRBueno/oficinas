from django.db import models

# Create your models here.
class Recado(models.Model):
    nome = models.CharField(max_length=80,)
    email = models.EmailField()
    mensagem = models.TextField(default="")
    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nome