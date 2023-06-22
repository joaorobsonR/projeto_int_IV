from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    servico = models.CharField(max_length=20)
    telefone = models.CharField(max_length=30)
    salario = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome
