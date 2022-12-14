import cv2 as cv
import numpy as np


def cartoonize(img):
    greyCap = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    greyCap = cv.medianBlur(greyCap, 5)
    edges = cv.adaptiveThreshold(
        greyCap, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)

    color = cv.bilateralFilter(img, 9, 250, 250)
    cartoon = cv.bitwise_and(color, color, mask=edges)

    return cartoon


cap = cv.VideoCapture("../../assets/village.mp4")

if (cap.isOpened() == False):
    print("Error opening video ")

while (cap.isOpened()):
    frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    fps = int(cap.get(cv.CAP_PROP_FPS))

    ret, frame = cap.read()
    if ret == True:
        cv.imshow("Frame", frame)
        cartoonized = cartoonize(frame)
        cv.imshow("Frame Cartoonized", cartoonized)

        if cv.waitKey(26) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
