import cv2

cap = cv2.VideoCapture(0)

while True:
    flag, img = cap.read()
    # resize = cv2.resize(img, (800,600))
    if not flag:
        break 
    cv2.imshow("Video", img)
    
    if cv2.waitKey(1) &  0xFF == ord('x'):
        break