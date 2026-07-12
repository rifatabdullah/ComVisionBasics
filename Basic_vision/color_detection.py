import cv2
from cvzone.ColorModule import ColorFinder

cap = cv2.VideoCapture(0)
colorfin = ColorFinder(trackBar=True) # for searching color 


hsvVal = {}

while True:
    flag, img = cap.read()
    # resize = cv2.resize(img, (800,600))
    if not flag:
        break 
    
    imgCol, mask = colorfin.update(img,hsvVal) 
    
    imgStack = cvzone.stackImages([img,imgCol,mask],3,0.5)
    
    
    cv2.imshow("Color Detection", img)
    
    if cv2.waitKey(1) &  0xFF == ord('x'):
        break