import csv
import os
from datetime import datetime


log_file = "logs/events.csv"


# Create file if it doesn't exist
if not os.path.exists(log_file):

    with open(log_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "timestamp",
                "event",
                "score_added",
                "total_score",
                "details"
            ]
        )


def log_event(event, score_added, total_score, details=""):

    with open(log_file, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                datetime.now(),
                event,
                score_added,
                total_score,
                details
            ]
        )