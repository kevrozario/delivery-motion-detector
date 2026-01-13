import cv2 as cv
from ultralytics import YOLO

model = YOLO("models/best.pt")

#classify packages
def classify_package(frame):

    package_found = False
    
    results = model(frame, verbose=False)
    
    for r in results:
        for box in r.boxes:
            
            confidence_score = float(box.conf[0])
            
            if confidence_score >= 0.5:
                package_found=True
                
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv.rectangle(frame, (x1, y1), (x2, y2), (255, 0 , 0), 2)
                
                return frame, package_found
            
        
        
    return frame, package_found