import cv2
import imageio

class GifCamera:
    def __init__(self, gif_path):
        self.gif = imageio.mimread(gif_path)
        self.index = 0

    def read(self):
        if self.index >= len(self.gif):
            self.index = 0
        frame = self.gif[self.index]
        self.index += 1
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        return True, frame_bgr

    def start_camera(self):
        pass  # For compatibility with WebCamera interface

    def stop_camera(self):
        pass
