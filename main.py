from detector.yolo_detector import YOLODetector
import cv2

# Set the path to your GIF
gif_path = "art/ball_tracking.gif"  # You can also try "art/yellow_cruiser.gif", "rt/ball_tracking.gif"

if __name__ == "__main__":
    # Create YOLO detector with GIF path
    detector = YOLODetector(gif_path=gif_path)

    while True:
        result_frame = detector.detect()
        if result_frame is None:
            print("End of video or failed to read frame.")
            break

        # Display detection frame
        cv2.imshow("YOLO Detection", result_frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
