import json
from imdb import IMDb
import time 


ia = IMDb()

search = ia.get_top250_movies()

movies = []

actors = set()
genres = set()
start_time = time.time()  
for i in range(250):
    movie_id = search[i].movieID
    movie = ia.get_movie(movie_id)
    movie_info = {
        'title': movie['title'],
        'rating': movie['rating'],
        'release_date': movie['original air date'].split('(')[0].strip() if 'original air date' in movie else None,
        'genres': movie['genres'][:3] if 'genres' in movie else [],
        'actors': [actor['name'] for actor in movie['cast'][:3]] if 'cast' in movie else []
    }
    print(f"Movie: {i}")
    movies.append(movie_info)

    actors.update(movie_info['actors'])
    genres.update(movie_info['genres'])

end_time = time.time() 
with open('movies.json', 'w', encoding='utf-8') as json_file:
    json.dump(movies, json_file, ensure_ascii=False, indent=4)

actors_data = list(actors)
with open('actors.json', 'w', encoding='utf-8') as json_file:
    json.dump(actors_data, json_file, ensure_ascii=False, indent=4)

genres_data = list(genres)
with open('genres.json', 'w', encoding='utf-8') as json_file:
    json.dump(genres_data, json_file, ensure_ascii=False, indent=4)

print("All time: %.2f s" % (end_time - start_time))