from Scripts import knn, pandas_reading, moods
from pathlib import Path



def main():
    mood = 'Happy'.lower()

    average_vector = moods.MOOD[mood]

    songs_csv = Path('somewhere')

    song_list = pandas_reading.get_song_list(songs_csv)

    closest_songs = knn.get_closest_k(song_list, average_vector)






if __name__ == '__main__':
    main()