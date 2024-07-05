from django.urls import path
from apps.galeria.views import \
     index, imagem, buscar, nova_imagem, editar_imagem, deletar_imagem, filtro

urlpatterns = [
    # Algumas rotas recebem um número inteiro (int:) ou string (str:) como argumento que representa o "id" do objeto na qual está sendo chamado, ou o tipo de filtro 
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('nova-imagem', nova_imagem, name='nova_imagem'),
    path('editar-imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),
    path('deletar-imagem/<int:foto_id>', deletar_imagem, name='deletar_imagem'),
    path('filtro/<str:categoria>', filtro, name='filtro'),
]

