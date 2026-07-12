import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
from cvzone.Utils import findContours


cap = cv2.VideoCapture(0)
colorfin = ColorFinder(trackBar= False) # for searching color 


# hsvVal = {'hmin': 0, 'smin': 37, 'vmin': 95, 'hmax': 52, 'smax': 255, 'vmax': 255}


hsvVal = {'hmin': 17, 'smin': 29, 'vmin': 0, 'hmax': 56, 'smax': 253, 'vmax': 255} # body spr


while True:
    flag, img = cap.read()
    # resize = cv2.resize(img, (800,600))
    if not flag:
        break 
    
    imgCol, mask = colorfin.update(img,hsvVal) 
    imgCon, conFound = findContours(img,mask)
    if conFound:
        print(conFound[0]['center'])
    
    imgStack = cvzone.stackImages([img,imgCol,mask,imgCon],4,0.5)
    
    
    cv2.imshow("Color Detection", imgStack)
    
    if cv2.waitKey(1) &  0xFF == ord('x'):
        break