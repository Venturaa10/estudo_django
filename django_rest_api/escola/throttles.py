from rest_framework.throttling import AnonRateThrottle


class MatriculaAnonRateThrottle(AnonRateThrottle):
    ''' Classe responsavel por aplicar um rate de acesso a API da matricula '''
    rate = '5/days'

