from similiarity import euclidean_distance, pearson_correlation


def get_similar_users(target_user, data, metric='euclidean'):
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
    similar_users = get_similar_users(target_user, data)
    print(f"Similar Users: {similar_users}")  # Debug print

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

    print(f"Recommended Movies: {recommended_movies}")  # Debug print
    print(f"Anti-Recommended Movies: {anti_recommended_movies}")  # Debug print

    return recommended_movies, anti_recommended_movies
