import cv2
import mediapipe as mp

from src.features.gaze_estimation import estimate_gaze


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

    # Get frame size
    h, w, _ = frame.shape

    # Flip image like a mirror
    frame = cv2.flip(frame, 1)

    # Convert BGR -> RGB
    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    # Process face landmarks
    results = face_mesh.process(rgb_frame)


    if results.multi_face_landmarks:

        face_landmarks = results.multi_face_landmarks[0]

        landmarks = face_landmarks.landmark


        gaze = estimate_gaze(
            landmarks,
            w,
            h
        )


        cv2.putText(
            frame,
            f"Gaze: {gaze}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )


    cv2.imshow(
        "Gaze Detection",
        frame
    )


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



camera.release()
cv2.destroyAllWindows()