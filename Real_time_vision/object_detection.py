import cv2 
import cvzone

from ultralytics import YOLO

cap = cv2.VideoCapture(0)

model = YOLO("best1.pt")


'''💡 Computer Vision Insight

This is a good example of how YOLO outputs predictions. Each detection contains:

box.xyxy → Bounding box coordinates
box.conf → Confidence score (a probability from 0.0 to 1.0)
box.cls → Class index

Think of one detection like this:

Object detected
├── Bounding Box → (120, 50, 280, 310)
├── Confidence → 0.94
└── Class → 2 (Thumbs Up)

'''



while True:
    
    success, img = cap.read()
    
    result = model(img, stream=True) # yields a result at a time and don't take everything at once
    
    for i in result:
        for box in i.boxes:
            x1,y1,x2,y2 = map(int, box.xyxy[0]) # gives us the bounding box -- (x1,y1)-top left corner, (x2,y2)-top bottom corner -- int needed as it returns floating points
            
            width, height = x2-x1, y2-y1
            conf = int(box.conf[0]*100)
            
            if conf < 50 :
                continue
            cls = int(box.cls[0])
            name = model.names[cls]
            cvzone.cornerRect(img,(x1,y1,width, height))
            cvzone.putTextRect(img, f"{name} {conf}", (x1,y1-10), scale = 1)
    
    cv2.imshow("Object Detection ", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break


# from ultralytics import YOLO

# model = YOLO("yolo26s.pt")

# model.train(
#     data = "data.yml",
#     epochs = 50, # total iterations
#     imgsz = 640,
#     batch = 8 # per image at a time
# )