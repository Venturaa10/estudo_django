from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer
from rest_framework import viewsets, generics, filters # Importa viewsets, generics, filters
# Importa as autenticações de usuario, as linhas de autenticação estão configuradas em settings.
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

'''
--> Os nomes das classes seguem uma nomeclatura com a finalidade de manter boas praticas de legibilidade do codigo.
--> Os nomes das variaveis estão em um formato padrão para funcionalidade do codigo.
'''

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all() # Armazena os objetos do modelo.
    serializer_class = EstudanteSerializer # O Serializer responsavél pelo modelo
    # Adiciona os filtros na API REST.
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

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