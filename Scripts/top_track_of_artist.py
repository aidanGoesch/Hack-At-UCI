import json
import time
import urllib.parse
import urllib.request
import requests
import pandas as pd

# Main function is create_csv which takes in a string of the desired artist and will return the top
# songs of the artist

CLIENT_ID = 'b38bdc06ca494cd385eaf026a84f53fd'
CLIENT_SECRET = '4418182ed9b447e8a142063574c5c347'

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

def get_song_artist(artist: str):
    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/search?'
    # actual GET request with proper header
    artist_list = artist.split()
    artist_link = '%20'.join(artist_list)
    header = create_header()
    r = requests.get(BASE_URL + f'q={artist_link}&type=track&market=US&limit=50', headers = header)
    r = r.json()
    list_tracks = r['tracks']['items']
    ans = []
    for track in list_tracks:
        ans.append(get_song_features(track['id']))
    return ans
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

def create_csv(artist: str):
    try:
        artist_songs_tuple = get_song_artist(artist)
        df = pd.DataFrame(artist_songs_tuple, columns = ['track_id',
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
        df.to_csv('temp.csv')
    except:
        print('Something went wrong. Maybe you spelled the artist wrong.')

if __name__ == '__main__':
    create_csv('Lil Uzi Vert')


