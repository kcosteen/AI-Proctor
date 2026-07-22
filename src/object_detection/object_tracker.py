import cv2
from ultralytics import YOLO
import csv
from datetime import datetime
import os
import time


log_file = "logs/detections.csv"


# Create log file if it doesn't exist
if not os.path.exists(log_file):
    with open(log_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "timestamp",
                "object",
                "confidence"
            ]
        )
        
model = YOLO("yolov8n.pt")


# Objects we care about for proctoring
suspicious_objects = [
    "cell phone",
    "book",
    "tablet"
]


cap = cv2.VideoCapture(0)

prev_time = time.time()

while True:

    ret, frame = cap.read()

    if not ret:
        break


    results = model(
    frame,
    classes=[
        0,   # person
        63,  # laptop
        67,  # cell phone
        73   # book
    ]
)


    # Go through every detected object
    for box in results[0].boxes:

        # Get class ID
        class_id = int(box.cls[0])


        # Convert ID to name
        object_name = model.names[class_id]


        # Confidence score
        confidence = float(box.conf[0])


        if confidence > 0.6:

            print(
                object_name,
                round(confidence, 2)
            )


            if object_name in suspicious_objects:

                print(
                    "⚠️ WARNING:",
                    object_name,
                    "detected!"
                )


                with open(log_file, "a", newline="") as file:

                    writer = csv.writer(file)

                    writer.writerow(
                        [
                            datetime.now(),
                            object_name,
                            round(confidence, 2)
                        ]
                    )
    current_time = time.time()

    fps = 1 / (current_time - prev_time)

    prev_time = current_time

    # Display
    annotated = results[0].plot()

    cv2.putText(
        annotated,
        f"FPS: {int(fps)}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    

    cv2.imshow(
        "AI Proctor Object Detection",
        annotated
    )


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()