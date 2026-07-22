import cv2
import numpy as np


FACE_POINTS = {
    "nose": 1,
    "chin": 152,
    "left_eye": 33,
    "right_eye": 263,
    "left_mouth": 61,
    "right_mouth": 291
}


def calculate_head_pose(landmarks, width, height):

    # 3D model points of a generic face
    face_3d = np.array([
        [0.0, 0.0, 0.0],        # Nose
        [0.0, -330.0, -65.0],   # Chin
        [-225.0, 170.0, -135],  # Left eye
        [225.0, 170.0, -135],   # Right eye
        [-150.0, -150.0, -125], # Left mouth
        [150.0, -150.0, -125]   # Right mouth
    ], dtype=np.float64)

    face_2d = np.array([
        [
            landmarks[FACE_POINTS["nose"]].x * width,
            landmarks[FACE_POINTS["nose"]].y * height
        ],

        [
            landmarks[FACE_POINTS["chin"]].x * width,
            landmarks[FACE_POINTS["chin"]].y * height
        ],

        [
            landmarks[FACE_POINTS["left_eye"]].x * width,
            landmarks[FACE_POINTS["left_eye"]].y * height
        ],

        [
            landmarks[FACE_POINTS["right_eye"]].x * width,
            landmarks[FACE_POINTS["right_eye"]].y * height
        ],

        [
            landmarks[FACE_POINTS["left_mouth"]].x * width,
            landmarks[FACE_POINTS["left_mouth"]].y * height
        ],

        [
            landmarks[FACE_POINTS["right_mouth"]].x * width,
            landmarks[FACE_POINTS["right_mouth"]].y * height
        ]

    ], dtype=np.float64)   

    focal_length = width

    center = (
        width / 2,
        height / 2
    )


    camera_matrix = np.array(
        [
            [focal_length, 0, center[0]],
            [0, focal_length, center[1]],
            [0, 0, 1]
        ],
        dtype=np.float64
    )

    dist_coeffs = np.zeros((4, 1), dtype=np.float64)

    success, rotation_vector, translation_vector = cv2.solvePnP(
        face_3d,
        face_2d,
        camera_matrix,
        dist_coeffs
    )

    rotation_matrix, _ = cv2.Rodrigues(rotation_vector)
    
    angles, _, _, _, _, _ = cv2.RQDecomp3x3(rotation_matrix)

    pitch = angles[0]
    yaw = angles[1]
    roll = angles[2]

    return pitch, yaw, roll