import json

def normalize_titles(ratings):
    return {movie.lower(): rating for movie, rating in ratings.items()}


def normalize_data(data):
    return {user: normalize_titles(ratings) for user, ratings in data.items()}


def load_and_normalize_data(file_path):
    # Load the dataset from a JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Normalize the data
    normalized_data = normalize_data(data)

    return normalized_data


def save_normalized_data(data, file_path):
    # Save the normalized data back to a JSON file
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    input_file = 'movie_ratings.json'
    output_file = 'normalized_movie_ratings.json'
    normalized_data = load_and_normalize_data(input_file)
    save_normalized_data(normalized_data, output_file)
