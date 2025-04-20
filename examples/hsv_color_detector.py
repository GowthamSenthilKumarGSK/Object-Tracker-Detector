import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import color_tracker
import cv2

# Init camera
#cam = color_tracker.WebCamera(video_src=0)
#cam.start_camera()

from color_tracker.utils.gif_camera import GifCamera
cam = GifCamera("art/ball_tracking.gif")  # or "yellow_cruiser.gif" , "ball_tracking.gif"

# Init Range detector
detector = color_tracker.HSVColorRangeDetector(camera=cam)
lower, upper, kernel = detector.detect()

# Print out the selected values
# (best practice is to save as numpy arrays and then you can load it whenever you want it)
print("Lower HSV color is: {0}".format(lower))
print("Upper HSV color is: {0}".format(upper))
print("Kernel shape is:\n{0}".format(kernel.shape))
