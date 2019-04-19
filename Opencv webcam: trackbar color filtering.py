import cv2 as cv 
import numpy as np 

def nthn(X):
    pass

webcam = cv.VideoCapture(0)

cv.namedWindow("window2")

cv.createTrackbar("Hmin","window2",0,255,nthn)
cv.createTrackbar("Hmax","window2",0,255,nthn)
cv.createTrackbar("Smin","window2",0,255,nthn)
cv.createTrackbar("Smax","window2",0,255,nthn)
cv.createTrackbar("Vmin","window2",0,255,nthn)
cv.createTrackbar("Vmax","window2",0,255,nthn)
cv.setTrackbarPos("Hmax","window2",255)
cv.setTrackbarPos("Smax","window2",255)
cv.setTrackbarPos("Vmax","window2",255)

while True:
    _,frame = webcam.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    Hmin = cv.getTrackbarPos("Hmin","window2")
    Smin = cv.getTrackbarPos("Smin","window2")
    Vmin = cv.getTrackbarPos("Vmin","window2")
    Hmax = cv.getTrackbarPos("Hmax","window2")
    Smax = cv.getTrackbarPos("Smax","window2")
    Vmax = cv.getTrackbarPos("Vmax","window2")
    
    mins = np.array([Hmin,Smin,Vmin])
    maxs = np.array([Hmax,Smax,Vmax])
    binaried = cv.inRange(hsv,mins,maxs)
    filtered = cv.bitwise_and(frame,frame,mask = binaried)

    cv.imshow("window2",filtered)
    cv.imshow("window3",binaried)
    key = cv.waitKey(1)
    if key == ord("q"):
        cv.destroyAllWindows()
        break

