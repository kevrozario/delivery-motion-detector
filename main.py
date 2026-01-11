import cv2 as cv
import os
from dotenv import load_dotenv

load_dotenv()
rtsp = os.getenv("RTSP") #rtsp address is stored in .env

cap = cv.VideoCapture(rtsp) 

if not cap.isOpened():
    print("Error: RTSP stream could not be opened")
else:
    print("RTSP stream opened successfully")
    

#Open a window to view the live stream
while cap.isOpened():
    ret, frame = cap.read() #capture each frame
    if not ret:
        break

    cv.imshow("RTSP", frame) #display each frame

    #click "q" to exit stream window
    if cv.waitKey(1) == ord("q"):
        break


cap.release()
cv.destroyAllWindows()
