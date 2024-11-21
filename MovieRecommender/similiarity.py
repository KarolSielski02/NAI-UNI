import math
from scipy.stats import pearsonr


def euclidean_distance(user1, user2):
    common_movies = set(user1.keys()).intersection(set(user2.keys()))
    if not common_movies:
        return 0
    sum_of_squares = sum((user1[movie] - user2[movie]) ** 2 for movie in common_movies)
    return 1 / (1 + math.sqrt(sum_of_squares))


def pearson_correlation(user1, user2):
    common_movies = set(user1.keys()).intersection(set(user2.keys()))
    if len(common_movies) < 2:
        return 0
    ratings1 = [user1[movie] for movie in common_movies]
    ratings2 = [user2[movie] for movie in common_movies]
    return pearsonr(ratings1, ratings2)[0]
