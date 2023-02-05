from pathlib import Path
import sys

sys.path.insert(1, './Scripts')

import knn
from flask_app import app
import moods
import pandas_reading
import os

port = os.environ.get("PORT", 5001)
def main():
    mood = 'Happy'.lower()
    artist = artist_csv

    average_vector = moods.MOOD[mood]

    songs_csv = Path('somewhere')

    song_list = pandas_reading.get_song_list(songs_csv)
    artist_songs = pandas_reading.get_song_list(artist)

    artist_avg = knn.get_average_vector(artist_songs)

    weighted_avg = knn.account_for_artist_vector(average_vector, artist_avg)

    closest_songs = knn.get_closest_k(song_list, weighted_avg)





if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = port)