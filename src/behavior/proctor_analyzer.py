import time


class ProctorAnalyzer:

    def __init__(self):
        self.score = 0

        self.event_history = {}

        self.cooldown = 10


    def add_score(self, event):

        scores = {
            "No face detected": 20,
            "Multiple people detected": 40,
            "Looking away": 10,
            "Phone detected": 50
        }

        current_time = time.time()


        if event in self.event_history:

            last_time = self.event_history[event]

            if current_time - last_time < self.cooldown:
                return 0


        self.event_history[event] = current_time


        points = scores.get(event, 0)

        self.score += points


        return points



    def analyze(
        self,
        object_results,
        face_count,
        gaze
    ):

        events = []


        # Face checks
        if face_count == 0:
            events.append("No face detected")


        if face_count > 1:
            events.append("Multiple people detected")


        # Gaze checks
        if gaze is not None and gaze != "CENTER":
            events.append("Looking away")


        # Object checks
        for obj in object_results:

            if obj["label"] == "cell phone":
                events.append("Phone detected")


        return events
    
    def get_status(self):

        if self.score < 30:
            return "Normal"

        elif self.score < 70:
            return "Suspicious"

        else:
            return "High Risk"