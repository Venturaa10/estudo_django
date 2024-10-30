from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Estudante(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 50, blank=False)
    cpf = models.CharField(max_length = 11, unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length = 14)

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    NIVEL = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    )
    codigo = models.CharField(max_length = 10, unique = True, validators=[MinLengthValidator(3)])
    descricao = models.CharField(max_length = 100 ,blank = False)
    nivel = models.CharField(max_length = 1, choices = NIVEL ,blank = False,null = False, default = 'B')

    def __str__(self):
        return self.codigo
    

class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Verpestino'), 
        ('N', 'Noturno'),
    )
    # Cascade -> Quando um estudante for deletado, todas as matriculas associadas ao objeto (estudante) também serão deletadas
    estudante = models.ForeignKey(Estudante, on_delete = models.CASCADE) # Cria uma relação com o modelo Estudante
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE) # Cria uma relação com o modelo Curso
    periodo = models.CharField(max_length = 1, choices = PERIODO ,blank = False,null = False, default = 'M')