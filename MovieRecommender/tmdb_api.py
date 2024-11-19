import os
import requests
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_TOKEN")


def get_movie_details(movie_title):
    def fetch_details(path, language='pl'):
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
