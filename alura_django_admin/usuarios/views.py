from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms # Importando os objetos responsaveis pelas alterações e validações no formulario (tag 'form' no HTML)
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    form = LoginForms() # Instanciando o objeto LoginForms em uma variavel

    return render(request, 'usuarios/login.html', {'form': form})


def cadastro(request):
    form = CadastroForms() # Instanciando o objeto LoginForms em uma variavel

    if request.method == 'POST':
        form = CadastroForms(request.POST) # Pegando todas as informações do form acima, e armazenando em uma outra variavel também chamada 'form'

        if form.is_valid():
                
            if form['senha_1'].value() != form['senha_2'].value():
                ''' Se o valor da senha 1 for diferente da senha 2, o usuario será redirecionado novamente para o cadastro'''
                return redirect('cadastro')
            
            # Os nomes dentro dos colchetes devem ser as mesmas do objeto criado no arquivo 'forms' para trabalhar com formulario
            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value() #Como a senha 1 deve obrigatoriamente ser igual a senha 2, não há necessidade de pegar o valor da senha 2 

            if User.objects.filter(username=nome).exists():
                '''Se o nome de usuario informado no cadastro já existir no banco de dados, o usuario será redirecionado para a pagina de cadastro novamente
                "username" é o nome que aparece no arquivo de banco de dados -> em "auth_user" onde é exibido todos os usuarios cadastrados no admin
                '''
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                # Criando o usuario com as informações fornecidas
                username=nome,
                email=email,
                password=senha,
            )
            usuario.save() # Salvando o Usuario

            return redirect('login') # Redirecionando a pagina de login após o cadastro ser concluído com sucesso   
          
    return render(request, 'usuarios/cadastro.html', {'form': form})
    