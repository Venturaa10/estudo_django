from rest_framework import permissions
import copy


class CustomDjangoModelPermission(permissions.DjangoModelPermissions):
    ''' 
    Classe personalizada para aplicar permissões baseadas no modelo do Django no Django Rest Framework (DRF). 
    Esta classe estende "DjangoModelPermissions" e adapta as permissões para incluir a operação "GET"(visualizar) como parte do mapeamento padrão.
    Em settings e REST_FRAMEWORK: 
    'DEFAULT_PERMISSION_CLASSES': [
    'escola.permissions.CustomDjangoModelPermission', Para utilizar a classe.
    ]
    '''
    def __init__(self):
        self.perms_map = copy.deepcopy(self.perms_map)
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']