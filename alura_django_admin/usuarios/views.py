from django.shortcuts import render
from usuarios.forms import LoginForms # Importando o objeto LoginForms responsavel pelo formulario
# Create your views here.

def login(request):
    form = LoginForms() # Instanciando o objeto LoginForms em uma variavel

    return render(request, 'usuarios/login.html', {'form': form})


def cadastro(request):
    return render(request, 'usuarios/cadastro.html')
    