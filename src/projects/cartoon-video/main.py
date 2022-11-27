import cv2 as cv
import numpy as np

img = cv.imread("../../assets/legion.png")


greyCap = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
greyCap = cv.medianBlur(greyCap, 5)
edges = cv.adaptiveThreshold(
    greyCap, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)

color = cv.bilateralFilter(img, 9, 250, 250)
cartoon = cv.bitwise_and(color, color, mask=edges)

cv.imshow("Image", img)
cv.imshow("Cartoon", cartoon)

cv.imwrite("cartoon.jpg", cartoon)
cv.waitKey(0)
cv.destroyAllWindows()
