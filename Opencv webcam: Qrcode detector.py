#pip3 install pyzbar or pip install pyzbar
import pyzbar.pyzbar as pyz
import cv2 as cv 

webcam = cv.VideoCapture(0)

while True:
    _,frame = webcam.read()
    
    #the function that finds the Qr codes.this function gives a list.inside the list there is a class with QRcode data
    QRs = pyz.decode(frame)
    
    for QR in range (0,len(QRs)):
        cords = QRs[QR].rect
        #un comment the line bellow to see the class
        #print(QRs[QR]) 
        x,y,w,h = cords
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv.circle(frame,((int(x+w/2),int(y+h/2))),2,(255,0,0),2)
        print('Name:',QRs[QR].data,'Coordinates:',QRs[QR].rect)

    cv.imshow("window",frame)
    key = cv.waitKey(1)
    if ord("q")==key:
        break
        cv.destroyAllWindows() 