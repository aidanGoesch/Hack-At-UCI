from pathlib import Path
import knn
import moods
import pandas_reading
import top_track_of_artist

# get 3 songs from atist that fit the mood, then 7 from the big list


def get_display_song_list(artist: str, mood: str):
    l_mood = mood.lower()

    if artist == '':
        temp = 'Something went wrong.'

    temp = top_track_of_artist.create_csv(artist)

    songs_csv = Path('./CSVs/song_list.csv')

    average_vector = moods.MOOD[l_mood]

    artist_csv = Path('temp.csv')

    try:
        pandas_reading.get_song_list(artist_csv)
    except FileNotFoundError:
        temp = 'Something went wrong.'

    if temp != 'Something went wrong.':
        song_list = pandas_reading.get_song_list(songs_csv)
        artist_songs = pandas_reading.get_song_list(artist_csv)

        top_artist_songs = knn.get_closest_k(artist_songs, average_vector, 3)

        artist_avg = knn.get_average_vector(artist_songs)
        weighted_avg = knn.account_for_artist_vector(average_vector, artist_avg)

        other_songs = knn.get_random_songs(knn.get_closest_k(song_list, weighted_avg, 14), 7)

        closest_songs = top_artist_songs + other_songs

    else:
        average_vector = moods.MOOD[l_mood]
        song_list = pandas_reading.get_song_list(songs_csv)
        closest_songs = knn.get_random_songs(knn.get_closest_k(song_list, average_vector, 30), 10)

    return closest_songs

