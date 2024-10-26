from escola.models import Estudante, Curso, Matricula
from escola.serialazers import EstudanteSerializer, CursoSerializer, MatriculaSerializer
from rest_framework import viewsets # Importa viewsets

class EstudanteViewSet(viewsets.ModelViewSet):
    ''' Os nomes das variaveis são padrão de boa pratica'''
    queryset = Estudante.objects.all() # Armazena os objetos do modelo
    serializer_class = EstudanteSerializer # O Serializer responsavél pelo modelo

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer