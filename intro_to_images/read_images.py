import cv2

img = cv2.imread("zarif.jpg")
resized = cv2.resize(img, (800,600)) # resized the main image as it was so high res. comapared to my dispaly's

cv2.imshow("image", resized)
cv2.waitKey(3000)