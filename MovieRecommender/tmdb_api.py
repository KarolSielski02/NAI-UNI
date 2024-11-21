import os
import requests
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_TOKEN")


def get_movie_details(movie_title):
    """
    Pobiera szczegóły dotyczące filmu lub serialu na podstawie tytułu, korzystając z API TMDB.

    Funkcja najpierw wyszukuje dane jako film, a jeśli nie znajdzie wyników,
    ponawia próbę jako serial telewizyjny.

    Parametry:
        movie_title (str): Tytuł filmu lub serialu do wyszukania.

    Zwraca:
        tuple: Krotka zawierająca:
            - szczegóły filmu/serialu (dict) lub None, jeśli nie znaleziono wyników,
            - ścieżkę ('movie' lub 'tv'), określającą typ wyniku (film lub serial),
              lub None, jeśli nie znaleziono wyników.
    """
    def fetch_details(path, language='pl'):
        """
        Pomocnicza funkcja do wykonania żądania API TMDB dla określonej ścieżki.

        Parametry:
            path (str): Ścieżka w API określająca, czy wyszukiwać filmy ('movie') czy seriale ('tv').
            language (str): Kod języka do wyników wyszukiwania (domyślnie 'pl').

        Zwraca:
            tuple: Krotka zawierająca:
                - szczegóły pierwszego wyniku wyszukiwania (dict) lub None, jeśli brak wyników,
                - ścieżkę ('movie' lub 'tv') lub None, jeśli brak wyników.
        """
        url = f"https://api.themoviedb.org/3/search/{path}?query={movie_title}&include_adult=false&language={language}&page=1"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {TMDB_API_KEY}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            results = response.json().get('results')
            if results:
                return results[0], path
        return None, None

    # First attempt with movie search
    details, path = fetch_details('movie')
    if details:
        return details, path

    # Retry with TV search
    return fetch_details('tv')


def format_details(details, path):
    """
    Formatuje szczegóły filmu lub serialu do ujednoliconego słownika.

    Parametry:
        details (dict): Słownik zawierający szczegóły filmu lub serialu zwrócone przez API TMDB.
        path (str): Ścieżka określająca typ wyniku ('movie' dla filmu, 'tv' dla serialu).

    Zwraca:
        dict: Sformatowany słownik zawierający szczegóły filmu lub serialu:
            - 'title': Tytuł filmu/serialu.
            - 'overview': Opis filmu/serialu.
            - 'release_date': Data premiery.
            - 'rating': Średnia ocena.
        Jeśli typ wyniku nie jest rozpoznany, zwraca None.
    """
    if path == 'movie':
        return {
            'title': details.get('title', 'N/A'),
            'overview': details.get('overview', 'N/A'),
            'release_date': details.get('release_date', 'N/A'),
            'rating': details.get('vote_average', 'N/A')
        }
    elif path == 'tv':
        return {
            'title': details.get('name', 'N/A'),
            'overview': details.get('overview', 'N/A'),
            'release_date': details.get('first_air_date', 'N/A'),
            'rating': details.get('vote_average', 'N/A')
        }
    return None
