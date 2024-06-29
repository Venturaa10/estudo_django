from apps.galeria.models import Fotografia
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

def index(request):
    # Caso eu acrescente "-" antes de data_fotografia, será exibido a ordem inversa, do mais antigo ao mais recente
    if not request.user.is_authenticated:
        '''Se o usuario não estiver logado, ele sera redirecionado para a pagina de login'''
        messages.error(request, 'É necessario fazer o login para continuar!')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)

    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    '''get_object_or_404 -> Retorna o objeto que é o id do objeto no banco de dados, caso não encontre, retorna um erro 404'''
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):

    if not request.user.is_authenticated:
        '''Se o usuario não estiver logado, ele sera redirecionado para a pagina de login'''
        messages.error(request, 'É necessario fazer o login para continuar!')
        return redirect('login')

    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    
    if 'buscar' in request.GET:
        '''O "buscar" faz referencia ao "name" do input de busca'''
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            '''Faz referencia ao nome que estou buscando e o nome do objeto em que está sendo buscado'''
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
        
    return render(request, 'galeria/buscar.html', {"cards": fotografias})

def nova_imagem(request):
    return render(request, 'galeria/nova_imagem.html')

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass

