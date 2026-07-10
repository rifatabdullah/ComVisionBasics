import cv2

cap = cv2.VideoCapture("clock1.mp4")

while True:
    flag, img = cap.read()
    resize = cv2.resize(img, (800,600))
    if not flag:
        break 
    cv2.imshow("Video", img)
    
    cv2.waitKey(1)