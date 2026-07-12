import cv2
import cvzone
import numpy as np
from cvzone.Utils import  findContours


img = cv2.imread("shapes.jpg")
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


imgCanny = cv2.Canny(imgGrey,50,100)
imgdia = cv2.dilate(imgCanny,np.ones((5,5),np.uint8), iterations = 1)

#Finding Edges
''' Detecting Shapes using boundary or outline of an object  '''
# filter - basically filtering shapes and if it's Noen then it will return all shapes
imgCon, conFound = findContours(img,imgdia, filter= [10], drawCon = True)
 
 
print(conFound[0]['bbox'])

imgStack = cvzone.stackImages([img,imgGrey,imgCanny, imgdia, imgCon],3,0.5)

cv2.imshow("Image ", imgStack )
cv2.waitKey(0)