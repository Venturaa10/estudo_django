from galeria.models import Fotografia
from django.shortcuts import render

def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request):
    return render(request, 'galeria/imagem.html')