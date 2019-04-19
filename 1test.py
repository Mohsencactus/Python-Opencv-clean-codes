import cv2 as cv 

webcam = cv.VideoCapture(0)

while True: 
    _,frame = webcam.read()

     