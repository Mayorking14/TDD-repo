from datetime import datetime

movies = {}

def add_movie(movie_name):
    if movie_name in movies:
        return "movie already exist in list"
    else:
        movies[movie_name] = {
            "added_on": datetime.now(),
            "movie_rating": [],
            "movie_average_rating": []
                              }
        return f"{movie_name} added successfully"

def rate_a_movie(movie_name, rating):
    if movie_name in movies:
        movies[movie_name]["movie_rating"].append(rating)
        return
    else:
        return f"Movie {movie_name} doesn't exist"

def get_average_movie_rating(movie_name):
    if movie_name in movies:



