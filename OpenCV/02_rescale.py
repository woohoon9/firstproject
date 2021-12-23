import cv2 as cv

img = cv.imread('OpenCV/photos/family.jpg', 0)
window_name = 'img'
cv.imshow(window_name, img)
cv.waitKey(0)

capture = cv.VideoCapture('OpenCV/videos/dog_v_02.mp4')

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0] *scale)


    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

def changeRes(width, height):
    # Live video resolution change
    capture.set(3, width)
    capture.set(4, height)


resized_img = rescaleFrame(img)
cv.imshow(window_name, resized_img)
cv.waitKey(0)


# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame)
#     cv.imshow('dog_v_02', frame)
#     cv.imshow('dog_v_02_resized', frame_resized)
#     if cv.waitKey(1) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

    