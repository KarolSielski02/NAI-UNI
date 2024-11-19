import json
from recommendation import recommend_movies
from tmdb_api import get_movie_details, format_details
from normalize_data import load_and_normalize_data

# Load and normalize the dataset from a JSON file
data = load_and_normalize_data('movie_ratings.json')


def print_movie_details(movies):
    for movie in movies:
        details, path = get_movie_details(movie)
        if details:
            formatted_details = format_details(details, path)
            print(f"Title: {formatted_details['title']}")
            print(f"Overview: {formatted_details['overview']}")
            print(f"Release Date: {formatted_details['release_date']}")
            print(f"Rating: {formatted_details['rating']}")
            print('-' * 40)
        else:
            print(f"Details not found for movie: {movie}")  # Debug print


target_user = "Tomasz Wasielewski"
recommended_movies, anti_recommended_movies = recommend_movies(target_user, data)

print("Recommended Movies:")
print_movie_details(recommended_movies)

print("Anti-Recommended Movies:")
print_movie_details(anti_recommended_movies)
