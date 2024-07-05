from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia # Esse formulario faz referencia a o modelo 'Fotografia'
        exclude = ['publicada'] # Atributo(s) do modelo 'Fotografia' que não será incluído no formulario        
        labels = {
            # Aqui realizo as alterações dos nomes dos atributos para como devem ser exibidos no template / HTML
            # "nome_atributo": "alteração"
            'descricao': 'Descrição',
            'data_fotografia': 'Data de Registro',
            'usuario': 'Usuário',

        }
        widgets = {
        'nome': forms.TextInput(attrs={'class':'form-control'}),
        'legenda': forms.TextInput(attrs={'class':'form-control'}),
        'categoria': forms.Select(attrs={'class':'form-control'}),
        'descricao': forms.Textarea(attrs={'class':'form-control'}),
        'foto': forms.FileInput(attrs={'class':'form-control'}),
        'data_fotografia': forms.DateInput(
            format = '%d/%m/%y', # O formato em que a data será exibida
            attrs={
                'type':'date',
                'class':'form-control'
            } 
        ),
        'usuario': forms.Select(attrs={'class':'form-control'}),
        }
