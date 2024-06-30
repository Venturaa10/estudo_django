from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages


def index(request):
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
        
    return render(request, 'galeria/index.html', {"cards": fotografias})


def nova_imagem(request):
    if not request.user.is_authenticated:
        '''Se o usuario não estiver logado, ele sera redirecionado para a pagina de login'''
        messages.error(request, 'É necessario fazer o login para continuar!')
        return redirect('login')
    
    form = FotografiaForms()

    if request.method == 'POST':
        '''
        request.POST -> Contém os dados enviados através dos campos do formulário que não são arquivos (ou seja, campos de texto, seleção, etc.).
        request.FILES -> Contém os arquivos enviados através dos campos do tipo 'file' - 'input type="file"', ondem no arquivo forms.py, o atributo "foto" é do tipo "FileInput"
        '''
        form = FotografiaForms(request.POST, request.FILES) 

        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index')


    return render(request, 'galeria/nova_imagem.html', {'form': form})


def editar_imagem(request, foto_id):
    '''Metodo responsavel por alterar as informações do objeto identificado pelo o id'''

    fotografia = Fotografia.objects.get(id=foto_id) # Variavel responsavél por pegar o "id" do objeto dentro do models "Fotografia"   

    form = FotografiaForms(instance=fotografia) # Instanciando no formulario "FotografiaForms" as informações do objeto no qual está sendo identificado pelo proprio "id" do objeto, ou seja, o formulario é autopreenchido com as informações de determinado objeto que é identificado pelo "id"

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia) # Criando uma nova instancia do formulario, agora com os dados recebidos, além da verificação das informações de input, também vincula a instancia "fotografia" / "id"

        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')

            return redirect('index')
        
    return render(request, 'galeria/editar_imagem.html', {'form':form, 'foto_id': foto_id})


def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)

    fotografia.delete() # Deletando o objeto do banco de dados
    messages.success(request, 'Fotografia deletada com sucesso!')
    return redirect('index')


def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True, categoria=categoria)

    # O nome é "cards", pois na views index o proprio template index já espera uma variavel chamada "cards" que contém fotografias
    return render(request, 'galeria/index.html', {'cards': fotografias})