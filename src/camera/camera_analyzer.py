import cv2
import time
from datetime import datetime

camera = cv2.VideoCapture(0)


previous_time = 0


while True:

    ret, frame = camera.read()

    if not ret:
        break


    # Calculate FPS
    current_time = time.time()

    fps = 1 / (current_time - previous_time)

    previous_time = current_time

    timestamp = datetime.now().strftime("%H:%M:%S")

    # Add FPS text
    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        timestamp,
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    cv2.imshow("Camera Analyzer", frame)


    key = cv2.waitKey(1)

    if key == ord('s'):
        cv2.imwrite(
            "screenshot.jpg",
            frame
        )
        print("Screenshot saved")

    if key == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()