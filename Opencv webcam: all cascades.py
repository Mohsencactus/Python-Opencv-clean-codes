import cv2 as cv
def detector(X):
   #Cascades :
    #Face #1 frontalface_alt
    if X == 1:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_frontalface_alt.xml')
    
    #Face #2 frontalface_alt2
    elif X == 2:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_frontalface_alt2.xml')
    
    #Face #3 frontalface_alt_tree
    elif X == 3:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_frontalface_alt_tree.xml')
    
    #Face #4 frontalface_default
    elif X == 4:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_frontalface_default.xml')
    
    #Face #5 profileface
    elif X == 5:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_profileface.xml')

    #Eye #1 eye_tree_eyeglasses
    elif X == 6:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_eye_tree_eyeglasses.xml')
    
    #Eye #2 eye
    elif X == 7:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_eye.xml')

    #Eye #3 lefteye_2splits
    elif X == 8:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_lefteye_2splits.xml')

    #Eye #4 righteye_2splits
    elif X == 9:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_righteye_2splits.xml')

    #Cat face #1 frontalcatface_extended
    elif X == 10:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_frontalcatface_extended.xml')

    #Cat face #2 frontalcatface
    elif X == 11:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_frontalcatface.xml')
    
    #Body #1 fullbody
    elif X == 12:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_fullbody.xml')

    #Body #2 lowerbody
    elif X == 13:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_lowerbody.xml')

    #Body #3 upperbody
    elif X == 14:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_upperbody.xml')

    #Licence plate #1 licence_plate_rus_16stages
    elif X == 15:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_licence_plate_rus_16stages.xml')

    #Licence plate #2 russian_plate_number
    elif X == 16:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_russian_plate_number.xml')

    #Smile #1 smile
    elif X == 17:
        cascade = cv.CascadeClassifier('/home/mohsencactus/Github Python/Python Opencv-start/Haarcascade/haarcascade_smile.xml')
   #framing and other stuff
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
print('')
print('Hello !Please choose the cascade based on the options given below:')
print('Option 1: Face #1 frontalface_alt')
print('Option 2: Face #2 frontalface_alt2')
print('Option 3: Face #3 frontalface_alt_tree')
print('Option 4: Face #4 frontalface_default')
print('Option 5: Face #5 profileface')
print('Option 6: Eye #1 eye_tree_eyeglasses')
print('Option 7: Eye #2 eye')
print('Option 8: Eye #3 lefteye_2splits')
print('Option 9: Eye #4 righteye_2splits')
print('Option 10: Cat face #1 frontalcatface_extended')
print('Option 11: Cat face #2 frontalcatface')
print('Option 12: Body #1 fullbody')
print('Option 13: Body #2 lowerbody')
print('Option 14: Body #3 upperbody')
print('Option 15: Licence plate #1 licence_plate_rus_16stages')
print('Option 16: Licence plate #2 russian_plate_number')
print('Option 17: Smile #1 smile')
print('')
while True:
    X = int(input("Choose your desigered option: "))
    detector(X)
    