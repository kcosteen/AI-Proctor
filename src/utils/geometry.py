import math

def distance(point1, point2):
    """
    Calculate the Euclidean distance between two (x, y) points.
    """

    return math.sqrt(
        (point2[0] - point1[0]) ** 2 +
        (point2[1] - point1[1]) ** 2
    )