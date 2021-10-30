from curses import meta
from pyexpat import model
from django.forms import fields
from rest_framework.serializers import ModelSerializer
from clientes.models import Cliente

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class ClienteFilterSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"