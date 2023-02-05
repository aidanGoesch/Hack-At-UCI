from pathlib import Path
import knn
import moods
import pandas_reading
import top_track_of_artist


def get_display_song_list(artist: str, mood: str):
    mood = mood.lower()

    temp = top_track_of_artist.create_csv(artist)

    songs_csv = Path('somewhere')

    average_vector = moods.MOOD[mood]

    if temp != 'Something went wrong.':
        artist_csv = Path('somewhere')

        song_list = pandas_reading.get_song_list(songs_csv)
        artist_songs = pandas_reading.get_song_list(artist_csv)

        artist_avg = knn.get_average_vector(artist_songs)

        weighted_avg = knn.account_for_artist_vector(average_vector, artist_avg)

        closest_songs = knn.get_closest_k(song_list, weighted_avg)
    else:
        average_vector = moods.MOOD[mood]
        song_list = pandas_reading.get_song_list(songs_csv)
        closest_songs = knn.get_random_songs(knn.get_closest_k(song_list, average_vector))

    return closest_songs

