from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms # Importando os objetos responsaveis pelas alterações e validações no formulario (tag 'form' no HTML)
# Create your views here.

def login(request):
    form = LoginForms() # Instanciando o objeto LoginForms em uma variavel

    return render(request, 'usuarios/login.html', {'form': form})


def cadastro(request):
    form = CadastroForms() # Instanciando o objeto LoginForms em uma variavel

    return render(request, 'usuarios/cadastro.html', {'form': form})
    