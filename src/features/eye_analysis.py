from src.utils.geometry import distance


def calculate_ear(eye_points, landmarks, width, height):
    """
    Calculate Eye Aspect Ratio (EAR)
    """

    points = []

    for index in eye_points:
        landmark = landmarks[index]

        x = int(landmark.x * width)
        y = int(landmark.y * height)

        points.append((x, y))

    p1, p2, p3, p4, p5, p6 = points

    vertical_1 = distance(p2, p6)
    vertical_2 = distance(p3, p5)

    horizontal = distance(p1, p4)

    ear = (vertical_1 + vertical_2) / (2.0 * horizontal)

    return ear