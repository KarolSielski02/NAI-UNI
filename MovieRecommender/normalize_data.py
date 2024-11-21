import json

def normalize_titles(ratings):
    """
    Normalizuje tytuły filmów, zmieniając je na małe litery.

    Parametry:
        ratings (dict): Słownik z ocenami filmów w formacie {tytuł: ocena}.

    Zwraca:
        dict: Słownik z tytułami filmów zapisanymi w małych literach.
    """
    return {movie.lower(): rating for movie, rating in ratings.items()}


def normalize_data(data):
    """
    Normalizuje dane użytkowników, zmieniając tytuły filmów na małe litery.

    Parametry:
        data (dict): Słownik zawierający dane użytkowników w formacie {użytkownik: {tytuł_filmu: ocena}}.

    Zwraca:
        dict: Słownik z danymi użytkowników, gdzie tytuły filmów są zapisane w małych literach.
    """
    return {user: normalize_titles(ratings) for user, ratings in data.items()}


def load_and_normalize_data(file_path):
    """
    Wczytuje dane z pliku JSON i normalizuje tytuły filmów.

    Parametry:
        file_path (str): Ścieżka do pliku JSON z ocenami filmów.

    Zwraca:
        dict: Znormalizowany słownik z ocenami użytkowników.
    """
    # Wczytaj dane z pliku JSON
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Normalizuj dane
    normalized_data = normalize_data(data)

    return normalized_data


def save_normalized_data(data, file_path):
    """
    Zapisuje znormalizowane dane do pliku JSON.

    Parametry:
        data (dict): Słownik z danymi użytkowników do zapisania.
        file_path (str): Ścieżka do pliku JSON, w którym zostaną zapisane dane.

    Zwraca:
        None
    """
    # Zapisz dane do pliku JSON
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    input_file = 'movie_ratings.json'
    output_file = 'normalized_movie_ratings.json'
    normalized_data = load_and_normalize_data(input_file)
    save_normalized_data(normalized_data, output_file)
