import cv2


camera = cv2.VideoCapture(0)


# Get camera width and height
width = int(camera.get(3))
height = int(camera.get(4))


# Create video writer
video = cv2.VideoWriter(
    "my_video.avi",
    cv2.VideoWriter_fourcc(*"XVID"),
    20,
    (width, height)
)


while True:

    ret, frame = camera.read()

    if not ret:
        break

    # Display camera
    cv2.imshow("Camera", frame)

    # Save frame to video
    video.write(frame)


    if cv2.waitKey(1) == ord('q'):
        break


camera.release()
video.release()
cv2.destroyAllWindows()