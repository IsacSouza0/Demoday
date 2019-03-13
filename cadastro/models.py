from django.db import models

# Create your models here.

class Cadastro(models.Model):
    nome = models.CharField(max_length=40)
    email = models.EmailField(blank=True, null= True)
    # telefone = models.ChatField(max_length=11)
    descricao = models.TextField(max_length=120)
    foto = models.ImageField(upload_to='', blank=True, null= True)

    def __str__(self):
        return self.nome