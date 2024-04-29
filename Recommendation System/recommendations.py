import datetime
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from movies_data import movies_data

def load_users_data():
    users_data = [
        {'name': 'User 1', 'ratings': {0: 5, 2: 4, 3: 3, 5: 5}},
        {'name': 'User 2', 'ratings': {1: 5, 2: 5, 4: 4, 6: 3}},
        {'name': 'User 3', 'ratings': {0: 3, 1: 4, 3: 5, 5: 4}},
    ]
    return users_data

def calculate_user_preferences(users_data):
    user_preferences = np.zeros((len(users_data), len(movies_data)))
    
    for i, user_data in enumerate(users_data):
        for movie_id, rating in user_data['ratings'].items():
            user_preferences[i, movie_id] = rating
    
    return user_preferences

def recommend_movie(mood, genre, users_data):
    user_preferences = calculate_user_preferences(users_data)
    
    similarity_scores = cosine_similarity(user_preferences, user_preferences)
    
    most_similar_user_index = np.argmax(similarity_scores[-1, :-1])
    
    similar_user_preferences = user_preferences[most_similar_user_index]
    
    genre_movies = [movie for movie in movies_data if movie['genre'] == genre]
    
    # Sort movies based on ranking
    genre_movies.sort(key=lambda x: x['ranking'])
    
    # Find movies that the most similar user liked
    recommended_movies = [movie['title'] for i, movie in enumerate(genre_movies) if similar_user_preferences[i] > 0]
    
    return recommended_movies

def greet_user():
    # Get the current time
    current_time = datetime.datetime.now()
    
    # Greet the user based on the time of the day
    if current_time.hour < 12:
        print("Good morning!")
    elif current_time.hour < 18:
        print("Good afternoon!")
    else:
        print("Good evening!")

def main():
    greet_user()
    user_name = input("What's your name? ")
    print(f"Hello, {user_name}!")
    
    mood = input("How are you feeling today (happy, neutral, or sad)? ")
    genre = input("What genre are you interested in (Thriller, Romance, War, Crime, or Documentary)? ")
    
    users_data = load_users_data()
    recommended_movies = recommend_movie(mood, genre, users_data)
    
    if recommended_movies:
        print("Recommended movies:")
        for movie in recommended_movies:
            print(movie)
    else:
        print("Sorry, no movies found for your preference.")

if __name__ == "__main__":
    main()
