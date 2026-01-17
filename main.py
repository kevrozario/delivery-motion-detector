import cv2 as cv
import os
from dotenv import load_dotenv
import time
from classify import classify_package, classify_food, classify_mail

load_dotenv()
rtsp = os.getenv("RTSP") #rtsp address is stored in .env

cap = cv.VideoCapture(rtsp) 

if not cap.isOpened():
    print("Error: RTSP stream could not be opened")
else:
    print("RTSP stream opened successfully")
    
cv.namedWindow("RTSP", cv.WINDOW_NORMAL)
cv.namedWindow("motion detector", cv.WINDOW_NORMAL)

#range of interest variables
x, y, w, h = 480, 50, 600, 1100 

#previous frame for motion detection
ret, frame1 = cap.read()
modified_frame1 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
modified_frame1 = cv.GaussianBlur(modified_frame1, (21, 21), 0)
roi_frame1 = modified_frame1[y:y+h, x:x+w]

#cooldown between detections
current_time = None
prev_time = 0
cooldown = 30


#Open a window to view the live stream
while cap.isOpened():
    
    ret, frame2 = cap.read() 
    if not ret:
        break
    
    #frame just for displaying to the user
    displayFrame=frame2.copy()
    cv.rectangle(displayFrame, (x,y), (x+w, y+h), (255, 0, 0), 2)
    cv.imshow("RTSP", displayFrame) 

    #current frame for motion detection
    modified_frame2 = cv.cvtColor(frame2, cv.COLOR_BGR2GRAY)
    modified_frame2 = cv.GaussianBlur(modified_frame2, (21, 21), 0)
    roi_frame2 = modified_frame2[y:y+h, x:x+w]
    
    #check differences in frames
    difference = cv.absdiff(roi_frame1, roi_frame2)
    thresh = cv.threshold(difference, 25, 255, cv.THRESH_BINARY)[1]
    detect_pixels = cv.countNonZero(thresh)
    
    current_time = time.time()
    
    if detect_pixels > 2000 and current_time - prev_time > cooldown:
        print("motion detected: ", detect_pixels)
        prev_time = current_time

    
    #cv.imshow("motion detector", thresh)
    
    #update previous frame
    roi_frame1 = roi_frame2
    
    #click "q" to exit stream window
    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
