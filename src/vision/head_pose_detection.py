import cv2
import mediapipe as mp

from src.features.head_pose import calculate_head_pose

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True
)

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces
    results = face_mesh.process(rgb_frame)

    # Draw detections
    if results.multi_face_landmarks:

        face_landmarks = results.multi_face_landmarks[0]

        landmarks = face_landmarks.landmark

        h, w, _ = frame.shape

        pitch, yaw, roll = calculate_head_pose(
            landmarks,
            w,
            h
        )

        cv2.putText(
        frame,
        f"Pitch: {pitch:.2f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

        cv2.putText(
            frame,
            f"Yaw: {yaw:.2f}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Roll: {roll:.2f}",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Head Pose Detection", frame)

    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()