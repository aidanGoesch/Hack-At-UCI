# pandas_reading.py: reads the song data from the file
import pandas as pd
from pathlib import Path
import numpy as np
import knn
import sys

np.set_printoptions(threshold=sys.maxsize)


def get_song_list(csv_path: Path) -> list[knn.MetricsVector]:
    """reads the csv file, turns the dataframe into a list. Then iterates through the list
    and makes a vector for each row in the song list"""
    songs = pd.read_csv(csv_path, low_memory=False, delimiter=',').values
    print(np.array(songs))

    vector_list = []
    for song in songs:
        v1, v2, v3, v4, v5, v6, v7, v8, v9, v10 = song[2:]
        vector_list.append(knn.MetricsVector(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, song_id=song[1]))

    return vector_list


if __name__ == "__main__":
    get_song_list(Path('C:\\Users\\dcspe\\Documents\\genres_v2.csv'))

