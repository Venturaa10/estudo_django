from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters # Importa viewsets, generics, filters
# Importa as autenticações de usuario, as linhas de autenticação estão configuradas em settings.
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from escola.throttles import MatriculaAnonRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly

'''
- Os nomes das classes seguem uma nomeclatura com a finalidade de manter boas praticas de legibilidade do codigo.
- Os nomes das variaveis estão em um formato padrão para funcionalidade do codigo.

Versionamento da API de Estudante
- Rota do Endpoint V1 da API: http://127.0.0.1:8000/estudantes/
- Rota do Endpoint V2 da API: http://127.0.0.1:8000/estudantes/?version=v2
'''


class EstudanteViewSet(viewsets.ModelViewSet):
    ''' 
    Descrição da View:

    - ViewSet do serializer de "EstudanteSerializer".
    - queryset -> Retorna todos os objetos do models de "Estudante" e realiza a ordenação com base no "id" dos objetos.
    
    # Filtros dos objetos da API.
        - filter_backends -> Define os filters permitidos endpoint da APIs.
        - ordering_fields -> Define quais campos podem ser usados para ordenar os resultados da API.
        - search_fields -> Define os campos onde é possivel realizar a busca do objeto na API.

    # Versionamento do Serializer
    - get_serializer_class():
        - Responsavel pela exibição do Serializer de acordo com a versão.
    '''
    queryset = Estudante.objects.all().order_by('id') # Armazena os objetos do modelo.
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

    def get_serializer_class(self):
        # Função responsavel por exibir a API de acordo com a sua versão.
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer


class CursoViewSet(viewsets.ModelViewSet):
    ''' 
    Descrição da View:

    - ViewSet do serializer de "CursoSerializer".
    - queryset -> Retorna todos os objetos do models de "Curso" e realiza a ordenação com base no "id" dos objetos.
    - serializer_class -> Serializer utilizado pelo viewSet.
    - permission_classes -> Tipo de autenticação para acessar a API.
    '''
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer
    # Adiciona autenticação de apenas leitura para todos e escrita apenas para usuarios autenticados.
    permission_classes = [IsAuthenticatedOrReadOnly]


class MatriculaViewSet(viewsets.ModelViewSet):
    '''
    Descrição da View:

    - ViewSet do serializer de "MatriculaSerializer"
    - queryset -> Retorna todos os objetos do models de "Matricula" e realiza a ordenação com base no "id" dos objetos.
    - throttle_classes -> Define o limite de acessos a API para usuarios autenticados e anonimos, quantidades estão configuradas em settings.
    - http_method_names -> Define quais metodos HTTP são permitidos nesse viewSet.
    '''
    queryset = Matricula.objects.all().order_by('id')
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"] # Metodos HTTP permitidos na API, nesse caso permitindo apenas leitura e criação de objetos na API.


# Utilizando o modulo "generics"
class ListaMatriculaEstudante(generics.ListAPIView):
    '''
    Descrição da View:

    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    '''
    def get_queryset(self):
        # Filtra as matriculas associadas ao estudante, onde o id é passado como parametro na URL
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset
    
    serializer_class = ListaMatriculasEstudanteSerializer


class ListaMatriculaCurso(generics.ListAPIView):
    '''
    Descrição da View:
    
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    '''
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset
    
    serializer_class = ListaMatriculasCursoSerializer
    