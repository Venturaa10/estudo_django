# Importa JsonResponse
from django.http import JsonResponse 

def estudantes(request):
    if request.method == 'GET':
        estudante = {
            'id': '1',
            'nome': 'Vincius'
        }
    # Transforma o dicionario em um tipo Json
    return JsonResponse(estudante)