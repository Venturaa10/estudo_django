from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaEstudante, ListaMatriculaCurso
from rest_framework import routers # Importa o routers para visualizar as APIs

'''
Explicação abaixa serve para tanto para estudantes quanto cursos
--> http://127.0.0.1:8000/estudantes/ -> Rota para listar e criar estudantes
--> http://127.0.0.1:8000/estudantes/2/ -> Rota para visualizar, atualizar ou excluir um estudante associado ao "id" na URL.
--> http://127.0.0.1:8000/estudantes/2/matriculas/ -> Rota para visualizar os cursos em que o estudante associado ao "id" está matriculado.
--> http://127.0.0.1:8000/cursos/1/matriculas/ -> Lista os estudantes que estão matriculados no curso associado ao "id" do curso.
'''

# Parametros -> prefixo, ViewSetName, basename='nome'
# Registro das rotas.
router = routers.DefaultRouter() # Gera automaticamente as rotas CRUD para cada ViewSet.
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')


'''
URL da Api Root
--> "as_views" - Informa que URL é utilizada apenas para visualização.
--> <int:pk> -> É o valor da ID dos objetos (Estudante e Curso) que está sendo buscado em ViewSet.
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaMatriculaCurso.as_view()),
]

