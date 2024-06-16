from django.db import models

# Create your models here.

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ('NEBULOSA', 'Nebulosa'), 
        ('ESTRELA', 'Estrela'),
        ('GALAXIA', 'Galaxia'),
        ('PLANETA', 'Planeta')
    ] 
    # Está sendo passado em tupla, pois é dessa forma que o metodo 'CharField' em 'categoria' entende

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False) 
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        '''Adicionar esse metodo str retornando o nome é uma boa pratica'''
        return f'Fotografia [nome={self.nome}]'