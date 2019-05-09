import cv2 as cv

#change the path to the cascade u desiger!
cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_eye.xml')
webcam = cv.VideoCapture(0)

while True:
    _,frame = webcam.read()
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    target = cascade.detectMultiScale(gray,1.2,4)
    
    for (x,y,w,h) in target:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
        cv.rectangle(frame, (x+w,y+h), (x,y+h+35), (255, 255, 0), cv.FILLED)
        cv.putText(frame, 'target', (x,y+h+28), cv.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)
        
    cv.imshow("frame",frame)
    key = cv.waitKey(1)
    if ord("q") == key:
        break
        cv.destroyAllWindows()