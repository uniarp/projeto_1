from django.db import models

class Tutor(models.Model):
    def __str__(self):
        return self.nome
    nome = models.CharField(max_length=80)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateTimeField("date published")
    observacao = models.CharField(max_length=8400)
    email = models.CharField(max_length=80)
    telefone = models.CharField(max_length=14)
    endereco = models.CharField(max_length=80)
    cons_cadun = models.CharField(max_length=100)