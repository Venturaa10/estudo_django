'''Arquivo responsavel pelas validações dos campos do serializers '''
import re
from validate_docbr import CPF

def cpf_invalido(numero_cpf):
    cpf = CPF()
    cpf_valido = cpf.validate(numero_cpf)
    return not cpf_valido

def nome_invalido(nome):
    return not nome.isalpha()

def celular_invalido(celular):
    # Padrão: 86 99999-9999
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    # Se padrão for true, retorna o valor encontrado, se não, retorna uma lista vazia.
    resposta = re.findall(modelo,celular) # Busca modelo na variavel celular.   
    print(resposta)
    return not resposta
        

