import numpy as np

p1 = [1, 2, 3]
p2 = [4, 5, 6]


def euclidean_distance(vector1, vector2):
    np_vector1 = np.asarray(vector1)
    np_vector2 = np.asarray(vector2)
    return np.sqrt(np.sum(np_vector1 - np_vector2) ** 2)


def manhattan_distance(vector1, vector2):
    np_vector1 = np.asarray(vector1)
    np_vector2 = np.asarray(vector2)
    return np.sum(np.abs(p1 - p2))


def chebyshev_distance(vector1, vector2):
    pass


def hamming_distance(vector1, vector2):
    pass


def cosine_distance(vector1, vector2):
    pass


def canberra_distance(vector1, vector2):
    pass



