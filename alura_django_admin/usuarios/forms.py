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

    