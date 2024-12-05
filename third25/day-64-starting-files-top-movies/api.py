import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY_TMDB = os.getenv('API_KEY_TMDB') 

class TMDBMovieFetcher:
    def __init__(self, query, ):
        """
        Inicializa el objeto con la API key y el término de búsqueda.
        """
        self.query = query
        self.id = 0
        self.url_movies = f"https://api.themoviedb.org/3/search/movie"
        self.url_movie_details = f'https://api.themoviedb.org/3/movie/'
        self.headers = {
            'accept': "application/json",
            'Authorization': f"Bearer {API_KEY_TMDB}"
        }
        self.results = []
        self.select_movie = []

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
        response = requests.get(url=self.url_movies, headers=self.headers, params=params)
        if response.status_code == 200:
            self.results = response.json().get('results', [])
        else:
            raise Exception(f"Error en la solicitud: {response.status_code} {response.text}")

    def get_titles_and_date(self):
        """
        Devuelve una lista de títulos únicos.
        """
        unique_titles = set()
        for movie in self.results:
            original_title = movie['original_title']
            original_language = movie['original_language']
            if original_title not in unique_titles and original_language == 'en':
                unique_titles.add(original_title)
                self.select_movie.append({
                    'id': movie['id'],
                    'original_title': movie['original_title'],
                    'release_date': movie['release_date']
                })
        return self.select_movie

    def get_movies_details(self, movie):
        url = f'{self.url_movie_details}/{movie}'
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            movie_data = response.json()
            return movie_data
        else:
            raise Exception(f"Error en la solicitud: {response.status_code} {response.text}")        
