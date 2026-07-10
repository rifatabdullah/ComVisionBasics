import cv2 

img = cv2.imread("intro_to_images/zarif.jpg")
resize = cv2.resize(img, (800,600))
blurimg = cv2.GaussianBlur(resize, (15,15), 0)
cv2.imshow("Image ✈️", resize)
cv2.imshow("Blur Image 👁️👁️", blurimg)
cv2.waitKey(0)