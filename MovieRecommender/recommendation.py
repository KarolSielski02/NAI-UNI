from similiarity import euclidean_distance, pearson_correlation


def get_similar_users(target_user, data, metric='euclidean'):
    """
     Znajduje użytkowników podobnych do podanego użytkownika na podstawie wskazanej metryki podobieństwa.

     Funkcja iteruje przez wszystkich użytkowników w danych (z wyłączeniem użytkownika docelowego)
     i oblicza poziom podobieństwa między użytkownikiem docelowym a innymi użytkownikami
     na podstawie ich ocen. Używa wybranej metryki (domyślnie odległość euklidesowa lub korelacja Pearsona),
     aby ocenić stopień podobieństwa.

     Parametry:
         target_user (str): Nazwa użytkownika, dla którego chcemy znaleźć podobnych użytkowników.
         data (dict): Słownik zawierający dane w formacie {użytkownik: {film: ocena}}.
         metric (str): Metryka podobieństwa do użycia. Możliwe wartości:
                       - 'euclidean' (odległość euklidesowa, domyślnie),
                       - 'pearson' (korelacja Pearsona).

     Zwraca:
         list: Posortowana lista krotek (użytkownik, wynik_podobieństwa),
               gdzie użytkownik to nazwa innego użytkownika, a wynik_podobieństwa to jego podobieństwo do użytkownika docelowego.
               Lista jest posortowana malejąco według wyniku podobieństwa (najbardziej podobni użytkownicy na początku).
     """
    similarity_scores = []
    for user, ratings in data.items():
        if user != target_user:
            if metric == 'euclidean':
                score = euclidean_distance(data[target_user], ratings)
            elif metric == 'pearson':
                score = pearson_correlation(data[target_user], ratings)
            similarity_scores.append((user, score))
    similarity_scores.sort(key=lambda x: x[1], reverse=True)
    return similarity_scores


def recommend_movies(target_user, data, num_recommendations=5, num_anti_recommendations=5):
    """
    Rekomenduje filmy na podstawie ocen użytkowników podobnych do użytkownika docelowego.

    Funkcja analizuje listę użytkowników podobnych do użytkownika docelowego
    (uzyskaną za pomocą funkcji `get_similar_users`) i sprawdza, które filmy ocenione przez tych użytkowników
    nie zostały jeszcze obejrzane przez użytkownika docelowego. Na tej podstawie generuje dwie listy:
    - Rekomendowane filmy (filmy z ocenami >= 7).
    - Filmy do unikania (anti-rekomendacje, filmy z ocenami < 5).

    Parametry:
        target_user (str): Nazwa użytkownika, dla którego generujemy rekomendacje.
        data (dict): Słownik zawierający dane w formacie {użytkownik: {film: ocena}}.
        num_recommendations (int): Maksymalna liczba filmów do rekomendacji. Domyślnie 5.
        num_anti_recommendations (int): Maksymalna liczba filmów do unikania (anti-rekomendacji). Domyślnie 5.

    Zwraca:
        tuple: Dwie listy:
            - recommended_movies (list): Lista `num_recommendations` filmów, które warto obejrzeć.
            - anti_recommended_movies (list): Lista `num_anti_recommendations` filmów, których warto unikać.
    """
    similar_users = get_similar_users(target_user, data)
    print(f"Similar Users: {similar_users}")

    recommended_movies = []
    anti_recommended_movies = []
    seen_movies = set(data[target_user].keys())

    for user, _ in similar_users:
        for movie, rating in data[user].items():
            if movie not in seen_movies:
                if rating >= 7 and len(recommended_movies) < num_recommendations:
                    recommended_movies.append(movie)
                elif rating < 5 and len(anti_recommended_movies) < num_anti_recommendations:
                    anti_recommended_movies.append(movie)
            if len(recommended_movies) >= num_recommendations and len(
                    anti_recommended_movies) >= num_anti_recommendations:
                break
        if len(recommended_movies) >= num_recommendations and len(anti_recommended_movies) >= num_anti_recommendations:
            break

    print(f"Recommended Movies: {recommended_movies}")
    print(f"Anti-Recommended Movies: {anti_recommended_movies}")

    return recommended_movies, anti_recommended_movies
