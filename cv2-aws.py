import numpy as np
import cv2
import boto3
import json

# Rekognition Detect faces
def detect_faces(photo):

    client=boto3.client('rekognition')

    response = client.detect_faces(
        Image={
            'Bytes': photo
        }, 
        Attributes=[
            'ALL'
        ]
    )
    return response

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        print(detect_faces(cv2.imencode('.jpg', frame)[1].tostring()))

# Release control of the webcam and close window     
cam.release()
cv2.destroyAllWindows()