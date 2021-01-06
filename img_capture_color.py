import cv2 
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

#define the resolution size....
def make_1080p():
	capture.set(3,1920)
	capture.set(4,1080)

while True:
	#return frame by frame.....
	ret,frame = capture.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=2,minSize=(20,20))
	for (x,y,w,h) in faces:
		print(x,w,y,h)
		roi_color = frame[y:y+h , x:x+w]
		
		cv2.imwrite('image_color.png',roi_color)
		color = (255,0,0)
		stroke = 2
		end_cord_x = x + w 
		end_cord_y = y + h
		cv2.rectangle(frame, (x, y), (end_cord_x,end_cord_y), color, stroke)
	#display the frames.
	cv2.imshow('frame',frame)
	#cv2.imshow('frame1',frame)
	if cv2.waitKey(20) & 0XFF == ord('q'):
		break

#relase the camera...
capture.release()
