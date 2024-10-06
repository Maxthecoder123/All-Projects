# car detection 
import cv2
cap = cv2.VideoCapture("vehicle.mp4")
car_cascade = cv2.CascadeClassifier("cars.xml")
# trained xml classidiers describes some features of objects we want to detence
while True:
    # read from video
    ret, frames = cap.read()
    gray = cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.1,1)
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Video2",frames)
    if cv2.waitKey(33)==27:
        break

cv2.destroyAllWindows()