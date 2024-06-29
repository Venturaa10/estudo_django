from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

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

    # A foto será armazenada com o caminha upload_to='caminho' que indica o ano, mes e dia.
    foto = models.ImageField(upload_to='fotos/%y/%m/%d/', blank=True)

    # Ao criar um novo item (Informação de uma nova foto na galeria do site), o padrão vai ser o item não ser publicado. Só após a opção for alterada para "True"
    # Será exibido um caixa de marcação ao criar uma nova fotografia em admin.
    publicada = models.BooleanField(default=False)  
    # Ao criar um novo item, será possivel incluir a hora e a data de criação, caso não seja informado, vai retornar a hora e a data daquele momento 
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey( 
        # Esse campo 'usuario' permite que cada instancia do modelo atual faça referencia a uma instancia do modelo 'User'
        
        to=User, # Define que o campo 'usuario' é uma chave estrangeira que se refere ao modelo 'User'
        on_delete=models.SET_NULL, # Caso o usuario responsavel por ter colocado determinada foto na galeria seja excluído, o campo será definido como nulo (null)
        null=True,
        blank=False,
        related_name='user', # Define o nome que será usado para referenciar este relacionamento reverso do lado do modelo User.
    )


    def __str__(self):
        '''Adicionar esse metodo str retornando o nome é uma boa pratica
        Por exemplo: Ao modificar algum item no banco de dados em admin, será exibida uma mensagem que retornara o nome desse objeto alterado
        '''
        return self.nome