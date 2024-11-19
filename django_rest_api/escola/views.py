from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters # Importa viewsets, generics, filters
# Importa as autenticações de usuario, as linhas de autenticação estão configuradas em settings.
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from escola.throttles import MatriculaAnonRateThrottle

'''
--> Os nomes das classes seguem uma nomeclatura com a finalidade de manter boas praticas de legibilidade do codigo.
--> Os nomes das variaveis estão em um formato padrão para funcionalidade do codigo.

Versionamento da API de Estudante
--> Rota do Endpoint V1 da API: http://127.0.0.1:8000/estudantes/
--> Rota do Endpoint V2 da API: http://127.0.0.1:8000/estudantes/?version=v2
'''

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all().order_by('id') # Armazena os objetos do modelo.
    # Codigo comentado para a função funcionar corretamente.
    # serializer_class = EstudanteSerializer # O Serializer responsavél pelo modelo
    # Adiciona os filtros na API REST.
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

    def get_serializer_class(self):
        # Função responsavel por exibir a API de acordo com a sua versão.
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"] # Metodos HTTP permitidos na API, nesse caso permitindo apenas leitura e criação de objetos na API.


# Utilizando o modulo "generics"
class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        # Filtra as matriculas associadas ao estudante, onde o id é passado como parametro na URL
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset
    
    serializer_class = ListaMatriculasEstudanteSerializer


class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset
    
    serializer_class = ListaMatriculasCursoSerializer