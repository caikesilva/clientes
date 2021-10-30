from rest_framework.viewsets import ModelViewSet
from clientes.api.serializers import ClienteFilterSerializer, ClienteSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend

class ClienteViewSet(ModelViewSet):
    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.filter(sexo='F', cidade='Meeren')
    
class ClienteFilterViewSet(ModelViewSet):
    serializer_class = ClienteFilterSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['sexo']

    def get_queryset(self):   
        return Cliente.objects.all().order_by('-nascimento')
    