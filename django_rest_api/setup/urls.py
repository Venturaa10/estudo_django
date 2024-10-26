from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet
from rest_framework import routers # Importa o routers para visualizar as APIs

router = routers.DefaultRouter()
# Parametros -> prefixo, ViewSetName, basename='nome'
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')

# URL da Api Root
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)) 

]
