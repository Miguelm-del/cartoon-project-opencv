import cv2 as cv
import numpy as np


def edge_mask(img, line_size, blur_value):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray_blur = cv.medianBlur(gray, blur_value)
    edges = cv.adaptiveThreshold(
        gray_blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, line_size, blur_value)
    return edges


cap = cv.VideoCapture("../../assets/village.mp4")
line_size = 3
blur_value = 3

if (cap.isOpened() == False):
    print("Error open video ")

while (cap.isOpened()):
    frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    fps = int(cap.get(cv.CAP_PROP_FPS))

    ret, frame = cap.read()
    if ret == True:
        cv.imshow("Frame", frame)
        cartoonized = edge_mask(frame, line_size, blur_value)
        cv.imshow("Frame Cartoonied", cartoonized)

        if cv.waitKey(26) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
