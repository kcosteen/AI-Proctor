import cv2


# Open webcam
camera = cv2.VideoCapture(0)


while True:

    # Read frame from camera
    ret, frame = camera.read()

    if not ret:
        print("Cannot open camera")
        break

    # Display frame
    cv2.imshow("My Camera", frame)


    # Press q to quit
    if cv2.waitKey(1) == ord('q'):
        break


# Release camera
camera.release()

# Close windows
cv2.destroyAllWindows()