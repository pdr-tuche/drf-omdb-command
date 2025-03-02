from .models import Filmes, Usuarios
from rest_framework import serializers


class FilmesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmes
        fields = '__all__'


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

