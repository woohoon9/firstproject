import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('OpenCV/photos/cat04.jpg')
cv.imshow('Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')


# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', mask)


# mask=cv.bitwise_and(gray, gray, mask=circle)
masked=cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask', masked)

#Grayscale histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])


# plt.figure()
# plt.title('Grayscale_Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Color Histogram

plt.figure()
plt.title('Colorscale_Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')


for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)