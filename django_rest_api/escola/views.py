from escola.models import Estudante, Curso
from escola.serialazers import EstudanteSerializer, CursoSerializer
from rest_framework import viewsets # Importa viewsets

class EstudanteViewSet(viewsets.ModelViewSet):
    ''' Os nomes das variaveis são padrão de boa pratica'''
    queryset = Estudante.objects.all() # Armazena os objetos do modelo
    serializer_class = EstudanteSerializer # O Serializer responsavél pelo modelo

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer