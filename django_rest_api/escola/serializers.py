from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_invalido # Importando as validações

''' 
--> Serializa os campos dos modelos para formatos como JSON, permitindo a exibição em APIs
--> Prepara os dados para serem enviados em uma API.
--> Os nomes das classes seguem uma nomeclatura com a finalidade de manter boas praticas de legibilidade do codigo.
 '''
class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante # Models na qual o serializer está associado.
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular'] # Campos que serão exibidos. 

    def validate(self, dados):
        '''Método responsavel por realizar as validações dos campos do estudante'''
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'O campo CPF deve ter um valor valido!'})
        
        if nome_invalido(dados['nome']):
            raise serializers.ValidationError({'nome':'O nome só deve conter letras'})
        
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular':'O campo celular precisa seguir o modelo: 86 99999-9999 respeitando traços e espaços.'})

        return dados

''' 
all -> Indica que vai ser usado todos os campos do modelo 
exclude = [ ] -> Indica que nenhum campo será excluído
'''
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'



class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []


class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao') # Busca valor do campo "dicionario" no objeto relacionado "curso" e define como somente leitura
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        # Função que captura a informação do valor do periodo
        return obj.get_periodo_display()
    

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']