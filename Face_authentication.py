#!/usr/bin/python36
import cv2
import numpy as np
model=cv2.face_LBPHFaceRecognizer.create()
model.read('face_recognizer.xml')

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detector(img, size=0.5):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi

def face_recognize():
	#to get image from file uncomment next line
	frame = cv2.imread('image.png')
	confidence  = 0
	#comment next 2 lines for reading from image
	#cap = cv2.VideoCapture(0)
	#ret, frame = cap.read()
	# cv2.imshow('hi',frame)
	# cv2.waitKey()
	# cv2.destroyAllWindows()
	image, face = face_detector(frame)

	try:
		face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

	    # Pass face to prediction model
	    # "results" comprises of a tuple containing the label and the confidence value
		results = model.predict(face)
		#print(results)
		if results[1] < 500:
			confidence = int( 100 * (1 - (results[1])/400) )
			display_string = str(confidence) + '% Confident it is User'
	
		cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)
		#print(confidence)
		if confidence > 75:
			cv2.putText(image, "Hey User", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
		#cv2.imshow('Face Recognition', image )
		#cv2.waitKey()
		#cv2.waitKey(1)
		#webbrowser.open('')
		#break
		else:
			cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)

		#cv2.imshow('Face Recognition', image )
	except:
		cv2.putText(image, "No Face Found", (220, 120) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
		cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
		#cv2.imshow('Face Recognition', image )
		pass
	
	return confidence

	#cv2.destroyAllWindows()

face_recognize()
