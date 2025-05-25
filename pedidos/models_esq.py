from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

try:
    from .utils import geocode_endereco
except ImportError:
    def geocode_endereco(endereco):
        pass

class Entregador(models.Model):
    class Meta:
        verbose_name = 'Entregador'
        verbose_name_plural = 'Entregadores'

    def __str__(self):
        pass

    def set_senha(self, senha_texto):
        pass
        
    def verificar_senha(self, senha_texto):
        pass

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('EM_PREPARO', 'Em Preparo'),
        ('EM_ENTREGA', 'Em Entrega'),
        ('ENTREGUE', 'Entregue'),
        ('CANCELADO', 'Cancelado')
    ]
    
    SABOR_CHOICES = [
        ('MUSSARELA', 'Mussarela'),
        ('CALABRESA', 'Calabresa'),
        ('PORTUGUESA', 'Portuguesa'),
        ('MARGHERITA', 'Margherita'),
        ('FRANGO_CATUPIRY', 'Frango com Catupiry'),
        ('QUATRO_QUEIJOS', 'Quatro Queijos'),
        ('PEPPERONI', 'Pepperoni'),
        ('VEGETARIANA', 'Vegetariana'),
        ('BACON', 'Bacon'),
        ('CHOCOLATE', 'Chocolate')
    ]

    def __str__(self):
        pass

    def save(self, *args, **kwargs):
        pass

    class Meta:
        ordering = ['-data_criacao']
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

class ParadaEntregador(models.Model):
    def __str__(self):
        pass
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Parada de Entregador'
        verbose_name_plural = 'Paradas de Entregadores'