import requests

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

def get_song_name(song_id: str) -> str:
    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/tracks/'

    # actual GET request with proper header
    headers = create_header()
    r = requests.get(BASE_URL + song_id + '?market=US', headers = headers)
    r = r.json()
    return r['name']

def song_id_list_to_song_name_list(id_list: list) -> list:
    for index in range(len(id_list)):
        id_list[index] = get_song_name(str(id_list[index].get_song_id()))
    return id_list

if __name__ == '__main__':
    pass
