from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    '''Essa classe é responsavél por alterar o modo de exibição do objeto no banco de dados'''
    # Nesse caso está passando as informações entre () parenteses
    list_display = ('id', 'nome', 'legenda', 'publicada') # Está retornando a id, nome e a legenda que são os atributos da classe

    list_display_links = ('id', 'nome') # Transforma o atributo em link, quando exibido no bando de dados, ficara com uma cor diferente (como link realmente), ao clicar sera redirecionado as informações do objeto

    search_fields = ('nome',) # As buscas no banco de dados será através do nome do objeto, a ',' no final é importante, pois o parametro deve ser passado como uma tupla

    list_filter = ('categoria', 'usuario') # Cria um tipo de filtro no admin, nesse caso o filtro será feito através da categoria da foto

    list_editable = ('publicada',) # O Publicada será exibido no admin sem precisar entrar nas informações do item e com possibilidade de edição na propria pagina / display

    list_per_page = 10 # Tamanho maximo de itens por pagina, ou seja, para todos os objetos dentro do models em admin, será exibido 10 por pagina

# Register your models here.
'''Registro da classe Fotografia no banco de dados do django admin'''
admin.site.register(Fotografia, ListandoFotografias)