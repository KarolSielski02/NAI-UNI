from flask import Flask, render_template, request
from recommendation import recommend_movies
from tmdb_api import get_movie_details, format_details
from normalize_data import load_and_normalize_data
import json

# Inicjalizacja aplikacji Flask
app = Flask(__name__)

# Wczytanie i normalizacja danych z pliku JSON
data = load_and_normalize_data('movie_ratings.json')


@app.route('/')
def index():
    """
    Wyświetla stronę główną aplikacji.

    Zwraca:
        str: Zrenderowany szablon `index.html`.
    """
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    """
    Obsługuje żądanie rekomendacji na podstawie danych wprowadzonych przez użytkownika.

    Proces:
    1. Pobiera nazwę użytkownika i jego oceny filmów z formularza.
    2. Parsuje oceny filmów i dodaje je do zbioru danych.
    3. Zapisuje zaktualizowany zbiór danych do pliku JSON.
    4. Generuje listy rekomendacji i anty-rekomendacji.
    5. Pobiera szczegóły rekomendowanych filmów z API TMDB.
    6. Wyświetla wyniki na stronie `recommendations.html`.

    Zwraca:
        str: Zrenderowany szablon `recommendations.html` z rekomendacjami.
    """
    user_name = request.form['name']
    user_ratings = request.form['ratings']

    # Parsowanie ocen filmów użytkownika
    user_ratings_dict = {}
    for line in user_ratings.split('\n'):
        movie, rating = line.split(':')
        user_ratings_dict[movie.strip().lower()] = int(rating.strip())

    # Dodanie ocen użytkownika do zbioru danych
    data[user_name] = user_ratings_dict

    # Dodanie ocen użytkownika do zbioru danych
    with open('movie_ratings.json', 'w') as f:
        json.dump(data, f, indent=4)

    # Dodanie ocen użytkownika do zbioru danych
    recommended_movies, anti_recommended_movies = recommend_movies(user_name, data)

    # Pobranie szczegółów rekomendowanych filmów z TMDB
    recommended_details = [format_details(*get_movie_details(movie)) for movie in recommended_movies]
    anti_recommended_details = [format_details(*get_movie_details(movie)) for movie in anti_recommended_movies]

    # Zrenderowanie strony z wynikami
    return render_template('recommendations.html', recommended=recommended_details,
                           anti_recommended=anti_recommended_details)


if __name__ == '__main__':
    # Uruchomienie aplikacji Flask w trybie debugowania
    app.run(debug=True)
