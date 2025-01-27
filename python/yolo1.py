import cv2
import torch
import numpy as np

model = torch.hub.load('ultralytics/yolov10', 'yolov10s')

video_path = '../refs/ny.mp4'
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    pred = np.squeeze(results.render())

    cv2.imshow('YOLO', pred)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
