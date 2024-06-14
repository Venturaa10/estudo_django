from galeria.models import Fotografia
from django.shortcuts import render, get_object_or_404

def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    '''get_object_or_404 -> Retorna o objeto que é o id do objeto no banco de dados, caso não encontre, retorna um erro 404'''
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})