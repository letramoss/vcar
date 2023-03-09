from django.db import models

# Create your models here.

class Carro(models.Model):
    placa = models.CharField(max_length=7,primary_key=True)
    marca = models.CharField(max_length=100)
    ano = models.DateField()
    modelo = models.CharField(max_length=100)
    data_compra = models.DateField()
    
class Cliente(models.Model):
    cpf = models.CharField(max_length=15,primary_key=True)
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=100)
    
class Aluguel(models.Model):
    codigo = models.AutoField(unique=True, primary_key=True)
    data_aluguel = models.DateField()
    data_entrega = models.DateField()
    devolucao = models.BooleanField("devolvido")
    diaria = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    placa = models.ForeignKey(Carro, on_delete=models.DO_NOTHING)
    
    
