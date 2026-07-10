import cv2 

img = cv2.imread("intro_to_images/zarif.jpg")
resize = cv2.resize(img, (800,600))

# [y1:y2, x1:x2]
CropImg = resize[100:300,20:300]


cv2.imshow("Image ✈️", resize)
cv2.imshow("Crop Image 👁️👁️", CropImg)
cv2.waitKey(0)