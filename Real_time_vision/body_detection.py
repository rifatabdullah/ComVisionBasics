import cv2 
from cvzone.PoseModule import PoseDetector

detector = PoseDetector()

cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    img = detector.findPose(img) # gives the bounding box to the body 
    lmlist, bbox = detector.findPosition(img) # gives the data from findPose()
    
    if bbox:
       center = bbox['center'] # bbox[0]['center] will track the first body infront of cam but without [0] it will track any body inforont of cam  
    
    cv2.imshow("Face Detection 👦🏻👦🏻", img)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break