"""
*****************************************************
*                   Color Tracker
*
* Author:       Gowtham
* Project:      HSV-based Object Tracking using OpenCV
* Description:  A color tracking system that allows dynamic HSV range
*               selection and real-time object detection.
* Version:      1.0.0
* Date:         April 2025
*
*****************************************************
"""

from .tracker.tracker import ColorTracker
from .utils import HSVColorRangeDetector
from .utils.camera import WebCamera

__author__ = "Gowtham"
__version__ = "1.0.0"
