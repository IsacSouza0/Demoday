from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome = models.CharField(max_length=40)
    email = models.EmailField()
    # telefone = models.ChatField(max_length=11)
    descrição = models.TextField(max_length=120)

    def __str__(self):
        return self.nome