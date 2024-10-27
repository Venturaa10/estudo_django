from escola.models import Estudante, Curso, Matricula
from escola.serialazers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer
from rest_framework import viewsets, generics # Importa viewsets, generics

'''
--> Os nomes das classes seguem uma nomeclatura com a finalidade de manter boas praticas de legibilidade do codigo.
'''

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

# Utilizando o modulo "generics"
class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        # Filtra as matriculas associadas ao estudante, onde o id é passado como parametro na URL
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaMatriculasEstudanteSerializer


class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaMatriculasCursoSerializer