import cv2
from ultralytics import YOLO
import numpy as np
import pygame
import threading

class YOLODetector:
    def __init__(self, gif_path, model_path="models/yolov5su.pt"):
        self.model = YOLO(model_path)
        self.cap = cv2.VideoCapture(gif_path)
        pygame.mixer.init()
        self.alert_sound = "alert.mp3"
        self.playing_alert = False

    def play_alert(self):
        if not self.playing_alert:
            self.playing_alert = True
            pygame.mixer.music.load(self.alert_sound)
            pygame.mixer.music.play()
            threading.Timer(2.0, self.reset_alert).start()  # prevent continuous looping

    def reset_alert(self):
        self.playing_alert = False

    def detect(self):
        ret, frame = self.cap.read()
        if not ret:
            return None

        results = self.model(frame, verbose=False)
        annotated_frame = frame.copy()

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                label = r.names[cls]

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(annotated_frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                if label in ['sports ball', 'skateboard']:
                    self.play_alert()

        return annotated_frame
