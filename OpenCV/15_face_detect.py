import cv2
import numpy as np


# imagePath = r'OpenCV\photos\lady.jpg'
# cascPath = r'OpenCV\haarcascade_frontalface_default.xml'

cascPath = r'OpenCV\haarcascade_frontalface_default.xml'
imagePath = r'OpenCV\faces_train\val\Ben_Afflek/09AFFLECK2-jumbo.jpg'

img = cv2.imread(imagePath)
cv2.imshow('Lady', img)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray_Lady', gray)


haar_cascade = cv2.CascadeClassifier(cascPath)

faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 3)

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w ,h) in faces_rect:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0) , thickness=2)

cv2.imshow('Detected_faces', img)

cv2.waitKey(0)