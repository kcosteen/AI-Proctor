import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        break

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        cv2.imwrite("my_photo.jpg", frame)
        print("Image saved")

    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()