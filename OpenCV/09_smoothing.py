import cv2 as cv

img = cv.imread('OpenCV/photos/cat04.jpg')
cv.imshow('Image', img)

# Averaging Blur
average = cv.blur(img, (7,7))
cv.imshow('Average_blur', average)


#Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian_Blur', gauss) 

#Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median_Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)

