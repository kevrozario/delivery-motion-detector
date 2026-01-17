import cv2 as cv
import os
from datetime import datetime

#save delivery image into a folder
def save_delivery_image(frame):
    os.makedirs("images", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"delivered@{timestamp}.jpg"
    filepath = os.path.join("images", filename)
    
    cv.imwrite(filepath, frame)