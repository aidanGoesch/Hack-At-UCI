import math
from typing import Self


K = 10


class MetricsVector:
    def __init__(self, danceability: float, energy: float, m_key: int, loudness: float,
                 speechiness: float, acousticness: float, instrumentalness: float,
                 liveness: float, valence: float, tempo: float, song_id: int=0):
        self.vector = (average_metric(danceability, 1),
                       average_metric(energy, 1),
                       average_metric(m_key, 1),
                       average_metric(loudness, 60),
                       average_metric(speechiness, 0.969),
                       average_metric(acousticness, 0.996),
                       average_metric(instrumentalness, 1),
                       average_metric(liveness, 1),
                       average_metric(valence, 1),
                       average_metric(tempo, 248.934))
        self.song_id = song_id

    def get_song_id(self) -> int:
        return self.song_id

    def get_vector(self) -> tuple:
        return self.vector

    def raw_assign(self, metrics_list: list[float]) -> None:
        """lets you forces assign values to the vector"""
        self.vector = tuple(metrics_list)

    def get_distance(self, vec1: Self) -> float:
        """gets the distance between 2 vectors"""
        squared_total = 0
        vec1_tuple = vec1.get_vector()
        vec2_tuple = self.get_vector()

        for i in range(len(vec1_tuple)):
            difference = vec2_tuple[i] - vec1_tuple[i]
            squared_total += math.pow(difference, 2)

        return abs(math.sqrt(squared_total))


def average_metric(metric: float, max_val: float | int) -> float:
    return round(metric / max_val, 5)


def get_average_vector(vector_list: list[MetricsVector]) -> MetricsVector:
    """Gets the average vector for a specific genre of music, which is
    what is used as the query parameter for getting the K closest vectors"""
    metrics_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # iterates through the vector list and adds every value to a
    for vec in vector_list:
        vector_tuple = vec.get_vector()
        for i in range(len(vector_tuple)):
            metrics_list[i] += vector_tuple[i]

    # iterates through the metrics list and divides each value by the length of the vector list
    for j in range(len(metrics_list)):
        metrics_list[j] = metrics_list[j]/len(vector_list)

    final_vector = MetricsVector(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    final_vector.raw_assign(metrics_list)

    return final_vector


def get_closest_k(vec_list: list[MetricsVector], query: MetricsVector) -> list[MetricsVector]:
    """returns the closest K number of vectors to the average vector"""
    vec_list.sort(key=lambda n: n.get_distance(query))
    return vec_list[:K]


def get_random_songs(vec_list: list[MetricsVector]) -> list[MetricsVector]:
    """randomly picks half the songs of the top K songs and adds them to a list"""
    final_list = []

    for i in range(K//2):
        random_song_index = random.randint(0, len(vec_list))
        final_list.append(vec_list[random_song_index])
        vec_list.pop(random_song_index)

    return final_list


def account_for_artist_vector(avg_vec: MetricsVector, artist_vec: MetricsVector) -> MetricsVector:
    """averages the artist vector and the average mood vector"""
    vector_list_1 = list(avg_vec.get_vector())
    vector_list_2 = list(artist_vec.get_vector())
    average_vector = []

    for i in range(len(vector_list_1)):
        average_vector.append(((2 * vector_list_1[i]) + vector_list_2[i])/3)

    temp_vec = MetricsVector(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    temp_vec.raw_assign(average_vector)

    return temp_vec


if __name__ == '__main__':
    vector1 = MetricsVector(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    vector2 = MetricsVector(1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    vector1.raw_assign([.5, .5, 0, 0, 0, 0, 0, 0, 0, 0])

    print(vector1.get_vector())

