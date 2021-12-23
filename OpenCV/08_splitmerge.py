import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('OpenCV/photos/boston.png')
cv.imshow('Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue= cv.merge([b, blank, blank])
green= cv.merge([blank, g, blank])
red= cv.merge([blank, blank, r])


cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged_Image', merged)

cv.waitKey(0)