import numpy as np

p1 = [1, 2, 3]
p2 = [4, 5, 6]


def euclidean(vector1, vector2):
    np_vector1 = np.asarray(vector1, dtype=float)
    np_vector2 = np.asarray(vector2, dtype=float)
    if np_vector1.shape != np_vector2.shape:
        raise ValueError("vectors must have same shape")
    return np.sqrt(np.sum(np_vector1 - np_vector2) ** 2)


def manhattan(vector1, vector2):
    np_vector1 = np.asarray(vector1, dtype=float)
    np_vector2 = np.asarray(vector2, dtype=float)
    if np_vector1.shape != np_vector2.shape:
        raise ValueError("vectors must have same shape")
    return np.sum(np.abs(np_vector1 - np_vector2))


def Minkowski(vector1, vector2, p):
    """
    For p != 1, 2
    """
    np_vector1 = np.asarray(vector1, dtype=float)
    np_vector2 = np.asarray(vector2, dtype=float)
    if np_vector1.shape != np_vector2.shape:
        raise ValueError("vectors must have same shape")
    return np.linalg.norm(np_vector1 - np_vector2, ord=p)


def chebyshev(vector1, vector2):
    np_vector1 = np.asarray(vector1, dtype=float)
    np_vector2 = np.asarray(vector2, dtype=float)
    if np_vector1.shape != np_vector2.shape:
        raise ValueError("vectors must have same shape")
    return np.linalg.norm(np_vector1 - np_vector2, ord=np.inf)


def hamming(vector1, vector2):
    np_vector1 = np.asarray(vector1, dtype=float)
    np_vector2 = np.asarray(vector2, dtype=float)
    if np_vector1.shape != np_vector2.shape:
        raise ValueError("vectors must have same shape")
    return int(np.sum(np_vector1 != np_vector2))


def hamming_normalized(vector1, vector2):
    np_vector1 = np.asarray(vector1)
    np_vector2 = np.asarray(vector2)
    if np_vector1.shape != np_vector2.shape:
        raise ValueError("vectors must have same shape")
    return float(np.mean(np_vector2 != np_vector2))


def cosine(vector1, vector2):
    np_vector1 = np.asarray(vector1, dtype=float)
    np_vector2 = np.asarray(vector2, dtype=float)
    if np_vector1.shape != np_vector2.shape:
        raise ValueError("vectors must have same shape")
    cos_sim = np.dot(np_vector1, np_vector2) / np.linalg.norm(np_vector1) * np.linalg.norm(np_vector2)
    return 1 - cos_sim


def canberra(vector1, vector2):
    pass
