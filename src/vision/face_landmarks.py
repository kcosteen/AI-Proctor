import cv2
import mediapipe as mp

# Initialize Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
)

# Drawing utilities
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            # Get frame dimensions
            h, w, _ = frame.shape

            # Landmark 1 (you can change the index later)
            landmark = face_landmarks.landmark[1]

            # Convert normalized coordinates to pixels
            x = int(landmark.x * w)
            y = int(landmark.y * h)

            # Draw a green circle at this landmark
            cv2.circle(frame, (x, y), 15, (0, 255, 0), -1)

            # Display the landmark index
            cv2.putText(
                frame,
                "1",
                (x + 10, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

            mp_draw.draw_landmarks(
                frame,
                face_landmarks,
                mp_face_mesh.FACEMESH_TESSELATION
            )

    cv2.imshow("Face Landmarks", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()