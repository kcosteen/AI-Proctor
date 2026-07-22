import cv2
import mediapipe as mp

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.5
)

# Drawing utility
mp_drawing = mp.solutions.drawing_utils

def detect_faces(frame):

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    face_results = face_detection.process(rgb_frame)

    face_count = 0

    if face_results.detections:
        face_count = len(face_results.detections)

        for detection in face_results.detections:
            mp_drawing.draw_detection(frame, detection)

    return face_results, face_count