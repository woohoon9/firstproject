import numpy as np
import cv2 as cv
import os

cascPath = os.path.normpath(r"C:\Users\jwoo\Desktop\PythonWorkspace\OpenCV\haarcascade_frontalface_default.xml")
imagePath = os.path.normpath(r"C:\Users\jwoo\Desktop\PythonWorkspace\OpenCV\faces_train\val\Madonna\GettyImages-494171282.jpg")
recogPath = os.path.normpath(r"C:\Users\jwoo\Desktop\PythonWorkspace\OpenCV\face_tranied.yml")

haar_cascade = cv.CascadeClassifier(r'OpenCV\haarcascade_frontalface_default.xml')

# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

people = ['Ben Afflek',  'Elton John', 'Madonna', 'Jerry Seinfield', 'Mindy Kaling']

# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read(recogPath)


img = cv.imread(imagePath)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 3)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness = 2)
    cv.rectangle(img, (x,y), (x+h, y+h), (0,255,0), thickness = 2)

cv.imshow('Detected_Face', img)

cv.waitKey(0)