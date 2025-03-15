# ## Task 2: Movie Recommendation System
#    1. Use this url https://developer.themoviedb.org/docs/getting-started/ to fetch information about movies.
#    2. Create a program that asks users for a movie genre and recommends a random movie from that genre.

import requests
import random

class MovieRecommender:
    BASE_URL = "https://api.themoviedb.org/3"
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.genres = self.get_genres()

    def get_genres(self):
        """Fetch available genres and return a dictionary {genre_name: genre_id}"""
        url = f"{self.BASE_URL}/genre/movie/list?api_key={self.api_key}"
        response = requests.get(url).json()
        return {genre["name"].lower(): genre["id"] for genre in response["genres"]}

    def get_movies_by_genre(self, genre_name):
        """Fetch movies by genre name"""
        genre_id = self.genres.get(genre_name.lower())
        if not genre_id:
            print("Invalid genre. Please choose from:", ", ".join(self.genres.keys()))
            return []
        
        url = f"{self.BASE_URL}/discover/movie?api_key={self.api_key}&with_genres={genre_id}"
        response = requests.get(url).json()
        return response.get("results", [])

    def recommend_movie(self, genre_name):
        """Pick a random movie from the chosen genre"""
        movies = self.get_movies_by_genre(genre_name)
        if not movies:
            return "No movies found for this genre."
        
        movie = random.choice(movies)
        return f" Recommended Movie: {movie['title']} \n Rating: {round((movie['vote_average']),2) if movie['vote_average']>0 else "N/A"} \n Overview: {movie['overview'] } "

def main():
    api_key = "2035d196c1b139bc97b9f6d9c3e65654"
    recommender = MovieRecommender(api_key)

    print("Please choose one genre from available genres:\n","\n".join(recommender.genres.keys()))
    genre = input("\nEnter a movie genre: ")
    print(recommender.recommend_movie(genre))

if __name__ == "__main__":
    main()
