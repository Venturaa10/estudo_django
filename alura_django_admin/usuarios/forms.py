# Arquivo proprio para trabalhar com formulario com o Django
from django import forms # Importando o modulo forms para trabalhar / lidar com formulario que o proprio Django fornece

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True, # Torna o preenchimento desse campo obrigatorio
        max_length= 100,
        widget=forms.TextInput(
            # Estilizando os labels do HTML através do proprio atributo do objeto
            attrs={
                'class': 'form-control', 
                'placeholder': 'Ex.: João Victor'
            }
        )
    )
    
    senha=forms.CharField(
        label='Senha',
        required=True, # Torna o preenchimento desse campo obrigatorio
        max_length=70,
        widget=forms.PasswordInput(
            # 
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha'
            }
        )
    )


class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro',
        required=True, # Torna o preenchimento desse campo obrigatorio
        max_length= 100,
        widget=forms.TextInput(
            # Estilizando os labels do HTML através do proprio atributo do objeto
            attrs={
                'class': 'form-control', 
                'placeholder': 'Ex.: João Victor'
            }
        )
    )

    email=forms.EmailField(
        label='Email',
        required=True, # Torna o preenchimento desse campo obrigatorio
        max_length= 100,
        widget=forms.EmailInput(
            # Estilizando os labels do HTML através do proprio atributo do objeto
            attrs={
                'class': 'form-control', 
                'placeholder': 'seuemail@tipo.com'
            }
        )
    )

    senha_1=forms.CharField(
        label='Senha',
        required=True, # Torna o preenchimento desse campo obrigatorio
        max_length=70,
        widget=forms.PasswordInput(
            # 
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha'
            }
        )
    )

    senha_2=forms.CharField(
        label='Confirme a sua senha',
        required=True, # Torna o preenchimento desse campo obrigatorio
        max_length=70,
        widget=forms.PasswordInput(
            # 
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha novamente'
            }
        )
    )

    def clean_nome_cadastro(self):
        '''Para validação é necessario seguir o formato acima: "clean_campo_para_validar(self)" 
        Validação para verificar se existem espaços em brancos no nome do usuario fornecido 
        '''
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip() # Retirando os caracteres de "espaço" do nome fornecido pelo usuario

            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            
            else:
                return nome
        
    def clean_senha_2(self):
        '''
        Validando se as senhas fornecidas são iguais, se a senha 2 é igual a senha 1
        Retorna uma mensagem no template ao usuario, em caso de senhas diferentes.
        '''
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('As senhas fornecidas não são iguais!') 
            
            else:
                return senha_2