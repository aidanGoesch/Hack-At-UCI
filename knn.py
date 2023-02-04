import math

K = 5


class MetricsVector:
    def __init__(self, danceability: float, energy: float, m_key: int, loudness: float,
                 speechiness: float, acousticness: float, instrumentalness: float,
                 liveness: float, valence: float, tempo: float):
        self.vector = (average_metric(danceability, 1),
                       average_metric(energy, 1),
                       average_metric(m_key, 1),
                       average_metric(loudness, 7.234),
                       average_metric(speechiness, 0.969),
                       average_metric(acousticness, 0.996),
                       average_metric(instrumentalness, 1),
                       average_metric(liveness, 1),
                       average_metric(valence, 1),
                       average_metric(tempo, 248.934))

    def get_vector(self) -> tuple:
        return self.vector


def average_metric(metric: float, max_val: float | int) -> float:
    return round(metric / max_val, 5)


def distance_between(vec1: MetricsVector, vec2: MetricsVector) -> float:
    """gets the distance between 2 vectors"""
    squared_total = 0
    vec1_tuple = vec1.get_vector()
    vec2_tuple = vec2.get_vector()

    for i in range(len(vec1_tuple)):
        difference = vec2_tuple[i] - vec1_tuple[i]
        squared_total += math.pow(difference, 2)

    return abs(math.sqrt(squared_total))



def get_closest_k(vec_list: list[MetricsVector], query: MetricsVector) -> list[MetricsVector]:
    """returns the closest K number of vectors to the average vector"""
    pass


if __name__ == '__main__':
    vector1 = MetricsVector(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    vector2 = MetricsVector(1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    print(distance_between(vector1, vector2))

