import cv2

img = cv2.imread("intro_to_images/zarif.jpg")
resized = cv2.resize(img, (800,600))

''' Put Text into Image
  > cv2.putText(
    img,            # Image to draw on
    text,           # Text string
    org,            # Bottom-left corner (x, y)
    fontFace,       # Font type
    fontScale,      # Font size
    color,          # Text color (B, G, R)
    thickness,      # Thickness of text
    lineType        # Line style (optional)
)
'''

cv2.putText(resized,"Hello!!",(300,200),cv2.FONT_HERSHEY_DUPLEX, 2, (100,50,0),2)



cv2.imshow("image", resized)
cv2.waitKey(0)