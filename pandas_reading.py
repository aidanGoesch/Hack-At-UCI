# pandas_reading.py: reads the song data from the file
import pandas as pd
from pathlib import Path
import numpy as np
import knn


def get_song_list(csv_path: Path) -> list[knn.MetricsVector]:
    column_names = []
    songs = pd.read_csv(csv_path, low_memory=False, delimiter=',').values
    # songs = songs.set_index('id', drop=False)
    print(songs)



if __name__ == "__main__":
    get_song_list(Path('C:\\Users\\dcspe\\Documents\\genres_v2.csv'))

