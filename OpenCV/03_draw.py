import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# img = cv.imread('OpenCV/photos/cat01.png')

#1, Paint the image a certain color
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('Red', blank)

#2. draw a rectangle
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,250,0), thickness = -1) 
# cv.imshow('Rectangle', blank)


#3 Draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness = -1)
# cv.imshow('Circle', blank)


#4. Draw a line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness = 5)
# cv.imshow('Line', blank)

#5 Write Text on image
cv.putText(blank, 'Hello, my name is Junghoon Woo!!!', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2 )
cv.imshow('Text', blank)

# cv.imshow('cat01', img)
cv.waitKey(0)
