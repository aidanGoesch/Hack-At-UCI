# Stores the Pre-determined average moods
import knn
import pandas_reading
from pathlib import Path


def get_average_mood_vectors() -> dict[str, knn.MetricsVector]:
    mood_list = ['angry', 'chill', 'happy', 'hype', 'sad']
    mood_dict = {}

    for mood in mood_list:
        csv_path = Path(f'./CSVs/{mood}.csv')

        vector_list = pandas_reading.get_song_list(csv_path)

        average_vector = knn.get_average_vector(vector_list)

        mood_dict[mood] = average_vector

    return mood_dict


MOOD = get_average_mood_vectors()

