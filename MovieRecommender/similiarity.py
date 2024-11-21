import math
from scipy.stats import pearsonr


def euclidean_distance(user1, user2):
    """
    Oblicza podobieństwo między dwoma użytkownikami na podstawie odległości euklidesowej ich ocen.

    Parametry:
        user1 (dict): Słownik zawierający oceny pierwszego użytkownika w formacie {film: ocena}.
        user2 (dict): Słownik zawierający oceny drugiego użytkownika w formacie {film: ocena}.

    Zwraca:
        float: Wartość podobieństwa w zakresie od 0 do 1, gdzie 1 oznacza maksymalne podobieństwo,
               a wartości bliższe 0 oznaczają większe różnice między ocenami.
               Jeśli użytkownicy nie mają wspólnych filmów, zwraca 0.
    """
    common_movies = set(user1.keys()).intersection(set(user2.keys()))
    if not common_movies:
        return 0
    sum_of_squares = sum((user1[movie] - user2[movie]) ** 2 for movie in common_movies)
    return 1 / (1 + math.sqrt(sum_of_squares))


def pearson_correlation(user1, user2):
    """
    Oblicza współczynnik korelacji Pearsona między dwoma użytkownikami na podstawie ich wspólnych ocen.

    Parametry:
        user1 (dict): Słownik zawierający oceny pierwszego użytkownika w formacie {film: ocena}.
        user2 (dict): Słownik zawierający oceny drugiego użytkownika w formacie {film: ocena}.

    Zwraca:
        float: Współczynnik korelacji Pearsona w zakresie od -1 do 1, gdzie:
               - 1 oznacza idealnie zgodne oceny,
               - 0 oznacza brak związku,
               - -1 oznacza idealnie przeciwne oceny.
               Jeśli użytkownicy nie mają wspólnych filmów, zwraca 0.
    """
    common_movies = set(user1.keys()).intersection(set(user2.keys()))
    if len(common_movies) < 2:
        return 0
    ratings1 = [user1[movie] for movie in common_movies]
    ratings2 = [user2[movie] for movie in common_movies]
    return pearsonr(ratings1, ratings2)[0]
