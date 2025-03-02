from rest_framework import viewsets
from .serializers import FilmesSerializer, UsuariosSerializer
from .models import Filmes, Usuarios


class FilmesViewSet(viewsets.ModelViewSet):
    queryset = Filmes.objects.all()
    serializer_class = FilmesSerializer


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
