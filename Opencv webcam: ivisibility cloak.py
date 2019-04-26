import cv2 as cv
import numpy as np
from time import sleep
#######################################
webcam = cv.VideoCapture(0)
_,background = webcam.read()
#######################################
hsvmin = np.array([98,100,28])
hsvmax = np.array([116,255,255])
#######################################
while True:
    _,frame = webcam.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    binaried = cv.inRange(hsv,hsvmin,hsvmax)
#######################################
    cloak = cv.morphologyEx(binaried, cv.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
    cloakrevers = cv.bitwise_not(cloak)
#######################################  
    backgoncloak = cv.bitwise_and(background,background,mask=cloak)
    cloakonframe = cv.bitwise_and(frame,frame,mask=cloakrevers)
    final = cv.addWeighted(backgoncloak,1,cloakonframe,1,0)
#######################################
    cv.imshow("frame",final)
    key = cv.waitKey(1)
    if key == ord("q"):
        cv.destroyAllWindows()
        break