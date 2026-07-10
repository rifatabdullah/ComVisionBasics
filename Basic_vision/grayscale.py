import cv2 

img = cv2.imread("intro_to_images/zarif.jpg")
resize = cv2.resize(img, (800,600))
cv2.imshow("Image ✈️", resize)
gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale Image ✈️🩶", gray)
cv2.waitKey(0)