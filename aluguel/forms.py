from django.forms import ModelForm
from .models import Carro, Cliente, Aluguel

class CarroForm(ModelForm):
    class Meta:
        model : Carro
        fields = ['placa','marca','ano','modelo','data_compra']

class ClienteForm(ModelForm):
    class Meta:
        model : Cliente
        fields = ['cpf','nome','data_nascimento','endereco']
        
class AluguelForm(ModelForm):
    class Meta:
        model : Aluguel
        fields = ['codigo','data_aluguel','data_entrega','devolucao','diaria','cpf','placa']
        
