from ultralytics import YOLO
import csv
from datetime import datetime
import os

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


def detect_objects(frame):

    yolo_results = model(
        frame,
        classes=[
            0,
            63,
            67,
            73
        ]
    )

    detected_objects = []

    for box in yolo_results[0].boxes:

        class_id = int(box.cls[0])

        object_name = model.names[class_id]

        confidence = float(box.conf[0])

        if confidence > 0.6:

            detected_objects.append({
                "label": object_name,
                "confidence": confidence
            })

            if object_name in suspicious_objects:

                with open(log_file, "a", newline="") as file:

                    writer = csv.writer(file)

                    writer.writerow([
                        datetime.now(),
                        object_name,
                        round(confidence, 2)
                    ])

    return yolo_results, detected_objects