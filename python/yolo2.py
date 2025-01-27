import cv2
from ultralytics import YOLO

model = YOLO('yolov8s.pt')

video_path = "../refs/ny.mp4"
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    success, frame = cap.read()

    if success:
        results = model(frame, device='mps')
        annotated_frame = results[0].plot()

        cv2.imshow("YOLOv8 Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
