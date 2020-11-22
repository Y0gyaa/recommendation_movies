import http.client
import json
import random

conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "7c6b23b89dmshb2c4667b24dd006p19235bjsnbd67f900a2dc",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }


def list_genres_all():
    """returns list of all genres"""
    conn.request("GET", "/title/list-popular-genres", headers=headers)
    res = conn.getresponse()
    data = res.read()
    in_json = data.decode("utf-8")
    resour = json.loads(in_json)
    genres = [item["description"] for item in  resour["genres"] ]
    return genres


def popular_movies(genre):
    """returns a random title id based on selected genre"""
    conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")
    url_genre = "/title/get-popular-movies-by-genre?genre=%%2Fchart%%2Fpopular%%2Fgenre%%2F" + genre.lower()
    conn.request("GET", url_genre , headers=headers)
    res = conn.getresponse()
    data = res.read()
    in_json = data.decode("utf-8")
    resour = json.loads(in_json)
    ttle_id = random.choice(resour)  
    return ttle_id


def ttle_naming(ttle_id):
    """returns title name for chosen genre and id"""
    conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")
    your_recomm= ttle_id.split('/')[2]
    url_ttle = "/title/get-details?tconst=" + your_recomm
    conn.request("GET", url_ttle, headers=headers)
    res = conn.getresponse()
    data = res.read()
    in_json = data.decode("utf-8")
    resour = json.loads(in_json)
    return resour
    