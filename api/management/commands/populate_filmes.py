import requests
from django.core.management.base import BaseCommand
from api.models import Filmes
import os
from django.core.cache import cache


class Command(BaseCommand):

    help = 'Popula a tabela de filmes com dados de uma API externa'

    CACHE_TIMEOUT = 60 * 60 * 24

    omdb_base_url = os.getenv('OMDB_BASE_URL')
    api_key = os.getenv('OMDB_API_KEY')

    parameters = {
        'apikey': api_key,
        't': 'avengers',
        'y': '2012'
    }

    def make_omdb_request(self):
        response = requests.get(
            f"{self.omdb_base_url}/", params=self.parameters)
        response.raise_for_status()
        return response.json()

    def handle(self, *args, **kwargs):
        if not self.omdb_base_url or not self.api_key:
            self.stdout.write(self.style.ERROR(
                "As variáveis de ambiente OMDB_BASE_URL e OMDB_API_KEY são necessárias!"))
            return

        cache_key = 'omdb_avengers_2012'
        filmes_data = cache.get(cache_key)

        if not filmes_data:
            filmes_data = self.make_omdb_request()
            cache.set(cache_key, filmes_data, self.CACHE_TIMEOUT)
            self.stdout.write(self.style.SUCCESS(
                "Dados armazenados no cache."))
        else:
            self.stdout.write(self.style.WARNING("Usando dados do cache."))

        nome = filmes_data.get("Title")
        genero = filmes_data.get("Genre")
        duracao = filmes_data.get("Runtime")

        if not nome or not genero or not duracao:
            self.stdout.write(self.style.ERROR(
                "Os dados retornados pela API estão incompletos!"))
            return

        if Filmes.objects.filter(nome=nome).exists():
            self.stdout.write(self.style.WARNING(
                f"O filme '{nome}' já existe no banco de dados."))
        else:
            Filmes.objects.create(
                nome=nome, genero=genero, duracao=duracao)
            self.stdout.write(self.style.SUCCESS(
                f"Tabela de filmes populada com sucesso!"))
