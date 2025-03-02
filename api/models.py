from django.db import models


class Filmes(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    duracao = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome} - {self.genero}'


class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    filmes = models.ManyToManyField(Filmes, blank=True)

    def __str__(self):
        return f'{self.nome} - {self.email}'
