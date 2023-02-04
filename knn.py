import math

K = 5
class MetricsVector:
    def __init__(self, danceability: float, energy: float, m_key: int, loudness: float,
                 speechiness: float, acousticness: float, instrumentalness: float,
                 liveness: float, valence: float, tempo: float):
        self.danceability = average_metric(danceability, 1)
        self.energy = average_metric(energy, 1)
        self.m_key = average_metric(m_key, 1)
        self.loudness = average_metric(loudness, 7.234)
        self.speechiness = average_metric(speechiness, 0.969)
        self.acousticness = average_metric(acousticness, 0.996)
        self.instrumentalness = average_metric(instrumentalness, 1)
        self.liveness = average_metric(liveness, 1)
        self.valence = average_metric(valence, 1)
        self.tempo = average_metric(tempo, 248.934)

    # getters and setters


def average_metric(metric: float, max_val: float | int) -> float:
    return round(metric/max_val, 5)

def distance_between(vec1: MetricsVector, vec2: MetricsVector) -> float:
    pass

def get_closest_k(vec_list: list[MetricsVector]) -> list[MetricsVector]:
    """returns the closest K number of vectors to the average vector"""
    pass



