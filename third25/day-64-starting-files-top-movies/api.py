import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY_TMDB = os.getenv('API_KEY_TMDB') 

class TMDBMovieFetcher:
    def __init__(self, query):
        """
        Inicializa el objeto con la API key y el término de búsqueda.
        """
        self.query = query
        self.url = f"https://api.themoviedb.org/3/search/movie"
        self.headers = {
            'accept': "application/json",
            'Authorization': f"Bearer {API_KEY_TMDB}"
        }
        self.results = []

    def fetch_movies(self):
        """
        Hace la solicitud al API y guarda los resultados.
        """
        params = {
            'query': self.query,
            'include_adult': 'false',
            'language': 'en-US',
            'page': 1
        }
        response = requests.get(url=self.url, headers=self.headers, params=params)
        if response.status_code == 200:
            self.results = response.json().get('results', [])
        else:
            raise Exception(f"Error en la solicitud: {response.status_code} {response.text}")

    def get_titles_and_date(self):
        """
        Devuelve una lista de títulos únicos.
        """
        title_and_date = []
        unique_titles = set()

        for movie in self.results:
            original_title = movie['original_title']
            if original_title not in unique_titles:
                unique_titles.add(original_title)
                title_and_date.append({
                    'id': movie['id'],
                    'original_title': movie['original_title'],
                    'release_date': movie['release_date']
                })
        return title_and_date

    def get_movies_details(self):
        pass

