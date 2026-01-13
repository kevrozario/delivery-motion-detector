import cv2 as cv
from ultralytics import YOLO

model = YOLO("models/best.pt")

def classify(frame):
