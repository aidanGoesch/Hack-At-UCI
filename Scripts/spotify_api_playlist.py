import json
import time
import urllib.parse
import urllib.request
import requests
import pandas as pd

CLIENT_ID = 'b38bdc06ca494cd385eaf026a84f53fd'
CLIENT_SECRET = '4418182ed9b447e8a142063574c5c347'

genres = {'happy': ('37i9dQZF1DXdPec7aLTmlC', '6HUHyoFBNNA3ZpssjlUqCL', '03KJbvju2CTk2Gks4K4lpp', '7CAsqQPQEemGgBQiGo6x93'),
          'sad': ('54NczufWOFmJ5jUVvRPxaF', '22kNFcCpmoyruXzVAXUAZS', '0DiIiLcScBTTTRgtRkwGxe', '3c0Nv5CY6TIaRszlTZbUFk'),
          'chill': ('7hJfYpKLDQwmeHIPTmNS5y', '7hJfYpKLDQwmeHIPTmNS5y', '2kg3XJlpeRL3MRgHwdAqB8'),
          'hype': ('6l3wEBANopjFYzZLppM8eJ', '3Qlo8PGJKE53FgTcIjuIvJ', '0874HuH6yEfOl0v14A13H2', '5X82XLmBmcl16PXuL7eYQ5'),
          'angry': ('457PRAhJMUXaS8s6Evh6Hd', '4zZpffTnguBELBde2Ar30Z')}

def get_token() -> str:
    AUTH_URL = 'https://accounts.spotify.com/api/token'
    # POST
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    })
    # convert the response to JSON
    auth_response_data = auth_response.json()
    # save the access token
    return auth_response_data['access_token']

def create_header() -> dict:
    access_token = get_token()
    headers = {
        'Authorization': 'Bearer {token}'.format(token = access_token)
    }
    return headers

header = create_header()

def get_song_features(song_id: str) -> tuple:
    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'
    # Track ID from the URI
    track_id = song_id
    # actual GET request with proper header
    headers = create_header()
    r = requests.get(BASE_URL + 'audio-features/' + track_id, headers = headers)
    r = r.json()
    dance = r['danceability']
    energy = r['energy']
    key = r['key']
    loudness = r['loudness']
    speechiness = r['speechiness']
    acousticness = r['acousticness']
    instrumentalness = r['instrumentalness']
    liveness = r['liveness']
    valence = r['valence']
    tempo = r['tempo']
    return track_id, dance, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo


def get_playlist(playlist_id: str) -> list:
    """ Returns a list of song ids in a playlist """
    BASE_URL = 'https://api.spotify.com/v1/playlists/'
    # actual GET request with proper header
    headers = create_header()
    r = requests.get(BASE_URL + playlist_id + '/tracks?market=US&fields=items(track(id))', headers = headers)
    r = r.json()
    items = r['items']
    ids = []
    for track in items:
        ids.append(track['track']['id'])
    return ids

def get_features_of_playlist(playlist_song_id_list: list) -> list['tuple']:
    """ Returns the features of a playlist"""
    playlist_features_list = []
    for song in playlist_song_id_list:
        playlist_features_list.append(get_song_features(song))
    return playlist_features_list

def get_features_for_genre():
    temp_genres = genres.copy()
    for genre, ids in temp_genres.items():
        features_of_genre = []
        for playlist_id in ids:
            song_list = get_playlist(playlist_id)
            features_of_songs_in_playlist = get_features_of_playlist(song_list)
            features_of_genre.extend(features_of_songs_in_playlist)
            time.sleep(20)
        no_dups = set(features_of_genre)
        list_no_dups = list(no_dups)
        temp_genres[genre] = list_no_dups
        print(genre)
    return temp_genres

if __name__ == '__main__':
    temp_genre = get_features_for_genre()
    for key, val in temp_genre.items():
        file = f'{key}.csv'
        df = pd.DataFrame(val, columns = ['track_id',
                                     'danceability',
                                     'energy',
                                     'key',
                                     'loudness',
                                     'speechiness',
                                     'acousticness',
                                     'instrumentalness',
                                     'liveness',
                                     'valence',
                                     'tempo'])
        df.to_csv(file)
