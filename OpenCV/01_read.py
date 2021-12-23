import cv2 as cv
img = cv.imread('OpenCV/cat01.jpg')
cv.imshow('cat01', img)
cv.waitKey(0)


# reading videos
# capture = cv.VideoCapture('OpenCV/videos/dog_v_02.mp4')
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('videos', frame)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()
