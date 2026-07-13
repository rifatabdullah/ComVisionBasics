import cv2 
from cvzone.HandTrackingModule import HandDetector 

from pprint import pprint


detector = HandDetector(detectionCon=0.8, maxHands = 2)

cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        pprint(hands[0])
        hand1 = hands[0]
        lmlist = hand1["lmList"] # findHands() return lmlist which a list of dicts . lmlist = landmark point of our hand 
        handType = hand1["type"] # determines left or right hand
 
    
    cv2.imshow("Hand Detection 🤚🏻🤚🏻", img)
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break