
p1 = [1,2,3]
p2 = [4,5,6]

def euclidean_distance(point1, point2):
    squared_sum = 0
    for i in range(len(point1)):
        difference = point1[i] - point2[i]
        squared_sum += difference**2
    return squared_sum**0.5

def manhattan_distance(point1, point2):
    abs_sum = 0
    for i in range(len(point1)):
        difference = point1[i] - point2[i]
        abs_sum += abs(difference)
    return abs_sum

def chebyshev_distance(point1, point2):
    pass

def hamming_distance(point1, point2):
    pass

def cosine_distance(point1, point2):
    pass

def canberra_distance(point1, point2):
    pass

euclidean_distance(p1, p2)