from ultralytics import YOLO
import cv2


model = YOLO("yolov8n.pt")


image = cv2.imread("my_photo.jpg")


results = model(image)


annotated = results[0].plot()


cv2.imshow(
    "YOLO Detection",
    annotated
)

cv2.waitKey(0)
cv2.destroyAllWindows()