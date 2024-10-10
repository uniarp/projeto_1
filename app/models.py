from django.db import models

class Tutor(models.Model):
    nome_tutor = models.CharField(max_length=100)
    cons_cadun = models.CharField(max_length=400)
    cpf = models.CharField(max_length=14)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_nacimento = models.DateField()
    
    def validacadun(cons_cadun) -> bool:
        return True

    def _str_(self):
        return self.nome_tutor

