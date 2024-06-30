from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms # Importando os objetos responsaveis pelas alterações e validações no formulario (tag 'form' no HTML)
from django.contrib.auth.models import User
from django.contrib import auth # Importando o modulo para realizar a autenticação
from django.contrib import messages # Importando o modulo responsavél por retornar mensagens ao usuario
# Create your views here.

def login(request):
    form = LoginForms() # Instanciando o objeto LoginForms em uma variavel

    if request.method == 'POST':
        form = LoginForms(request.POST) # Recria o formulario com os dados enviados pelo usuario, por isso é utilizado o "request.POST" como parametro

        if form.is_valid():
            '''Variaveis responsaveis por armazenar o valor do atributo em "form.py" da classe "LoginForms" na qual o usuario vai preencher'''
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            
            ''' 
            Tenta encontrar um usuário no banco de dados que tenha o nome de usuário "nome" e a "senha" senha. Se encontrar, retorna esse usuário. Se não encontrar, retorna None.

            Realiza a autenticação do usuario com o nome e a senha fornecidos
            Verifica se os dados fornecidos estão corretos
            '''
            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome} logado com sucesso!') # Retorna uma mensagem de sucesso em caso de login efetuado
                return redirect('index')
            else:
                messages.error(request, 'Erro ao efetuar login!') # Retorna uma mensagem de erro em caso de login não efetuado
                return redirect('login')
        
        else:
           pass

    return render(request, 'usuarios/login.html', {'form': form})


def cadastro(request):
    form = CadastroForms() # Instanciando o objeto LoginForms em uma variavel

    if request.method == 'POST':
        form = CadastroForms(request.POST) # Pegando todas as informações do form acima, e armazenando em uma outra variavel também chamada 'form'

        if form.is_valid():
            
            # Os nomes dentro dos colchetes devem ser as mesmas do objeto criado no arquivo 'forms' para trabalhar com formulario
            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha_1'].value() #Como a senha 1 deve obrigatoriamente ser igual a senha 2, não há necessidade de pegar o valor da senha 2 

            if User.objects.filter(username=nome).exists():
                '''Se o nome de usuario informado no cadastro já existir no banco de dados, o usuario será redirecionado para a pagina de cadastro novamente
                "username" é o nome que aparece no arquivo de banco de dados -> em "auth_user" onde é exibido todos os usuarios cadastrados no admin
                '''
                messages.error(request, 'Usuario já existe')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                # Criando o usuario com as informações fornecidas
                username=nome,
                email=email,
                password=senha,
            )
            usuario.save() # Salvando o Usuario

            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login') # Redirecionando a pagina de login após o cadastro ser concluído com sucesso   
          
    return render(request, 'usuarios/cadastro.html', {'form': form})
    

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso') 
    return redirect('login')