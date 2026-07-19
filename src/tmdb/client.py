#https://developer.themoviedb.org/reference/search-movie

from django.conf import settings
import requests

url = "https://api.themoviedb.org/3/genre/movie/list?language=en"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {settings.TMDB_API_KEY}"
}

"""
response = requests.get(url, headers=headers)

print(response.text)
"""
def search_movies(query : str, page : int = 1):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "query": query,
        "include_adult" : "false",
        "language" : "en-US", 
        "page" : page}
    
    response = requests.get (url, headers=headers, params = params)
    return response.json()

def movie_details(movie_id: int):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        "language" : "en-US", 
        }   
    response = requests.get (url, headers=headers)
    return response.json()