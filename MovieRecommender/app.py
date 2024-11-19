from flask import Flask, render_template, request
from recommendation import recommend_movies
from tmdb_api import get_movie_details, format_details
from normalize_data import load_and_normalize_data
import json

app = Flask(__name__)

# Load and normalize the dataset from a JSON file
data = load_and_normalize_data('movie_ratings.json')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    user_name = request.form['name']
    user_ratings = request.form['ratings']

    # Parse user ratings
    user_ratings_dict = {}
    for line in user_ratings.split('\n'):
        movie, rating = line.split(':')
        user_ratings_dict[movie.strip().lower()] = int(rating.strip())

    # Add user ratings to the dataset
    data[user_name] = user_ratings_dict

    # Save the updated dataset to the JSON file
    with open('movie_ratings.json', 'w') as f:
        json.dump(data, f, indent=4)

    # Get recommendations
    recommended_movies, anti_recommended_movies = recommend_movies(user_name, data)

    # Fetch movie details
    recommended_details = [format_details(*get_movie_details(movie)) for movie in recommended_movies]
    anti_recommended_details = [format_details(*get_movie_details(movie)) for movie in anti_recommended_movies]

    return render_template('recommendations.html', recommended=recommended_details,
                           anti_recommended=anti_recommended_details)


if __name__ == '__main__':
    app.run(debug=True)
