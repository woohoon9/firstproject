import cv2 as cv

img = cv.imread('OpenCV/photos/boston.png')
cv.imshow('Boston', img)

# converting to grayscale

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)

# Blur
blur=cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade(Unblurred Image)
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny_Edges', canny)

# Edge Cascade(blurred Image)
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny_Edges_Blur', canny)

# Dilating the image
dilated = cv.dilate(canny, (10,10), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (10,10), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)



cv.waitKey(0)