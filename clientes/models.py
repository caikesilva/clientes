from statistics import mode
from django.db import models

# Create your models here.

class Cliente(models.Model):
    SEXO = (
        ('M','Masculino'),
        ('F','Feminino')
    )
    nome = models.CharField(verbose_name="Nome", max_length=255)
    sobrenome = models.CharField(verbose_name="Sobrenome", max_length=255)
    sexo = models.CharField(verbose_name="Sexo", max_length=1, choices=SEXO, blank=False, null=False, default='M')
    altura = models.DecimalField(verbose_name="Altura"),
    peso = models.DecimalField(verbose_name="Peso"),
    nascimento = models.CharField(verbose_name="Nascimento", max_length=10)
    bairro = models.CharField(verbose_name="Bairro", max_length=255)
    cidade = models.CharField(verbose_name="Cidade", max_length=255)
    estado = models.CharField(verbose_name="Estado", max_length=255)
    numero = models.IntegerField(verbose_name="Numero")

    def __str__(self):
        nome_completo = f"{self.nome} {self.sobrenome}"
        return nome_completo
