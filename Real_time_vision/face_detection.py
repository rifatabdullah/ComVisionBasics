import cv2 
from cvzone.FaceDetectionModule import FaceDetector

detector = FaceDetector()

cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    img, bbox = detector.findFaces(img)
    if bbox:
        center = bbox[0]['center'] # will detect the first bounding box 
    
    cv2.imshow("Face Detection 👦🏻👦🏻", img)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break