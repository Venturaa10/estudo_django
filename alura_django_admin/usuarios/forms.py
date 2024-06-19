# Arquivo proprio para trabalhar com formulario com o Django
from django import forms # Importando o modulo forms que o proprio Django fornece

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True, # Torna o preenchimento desse campo obrigatorio
        max_length= 100
    )
    
    senha=forms.CharField(
        label='Senha',
        required=True, # Torna o preenchimento desse campo obrigatorio
        max_length=70,
        widget=forms.PasswordInput()
    )