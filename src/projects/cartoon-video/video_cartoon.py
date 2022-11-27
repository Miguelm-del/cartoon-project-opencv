import cv2 as cv
import numpy as np


def cartoonize(img, k):
    data = np.float32(img).reshape((-1, 3))
    print("shape of input data: ", img.shape)
    print('shape of resized data', data.shape)

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 20, 1.0)

    _, label, center = cv.kmeans(
        data, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    print(center)

    result = center[label.flatten()]
    result = result.reshape(img.shape)
    cv.imshow("result", result)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    edges = cv.adaptiveThreshold(
        gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 8)
    cv.imshow("edges", edges)

    blurred = cv.medianBlur(result, 3)
    cartoon = cv.bitwise_and(blurred, blurred, mask=edges)

    return cartoon


# img = cv.imread("../../assets/legion.png")
cap = cv.VideoCapture("../../assets/mylife.mp4")

# Method to convert image to image cartoonized

if (cap.isOpened() == False):
    print("Error opening video ")


while (cap.isOpened()):
    frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    print("w,h", frame_width, frame_height)

    fps = int(cap.get(cv.CAP_PROP_FPS))

    # fourcc = cv.VideoWriter_fourcc(*'FMP4')
    # outCap = cv.VideoWriter('outpy.mp4', fourcc, fps,
    #                    (frame_width, frame_height))

    ret, frame = cap.read()
    if ret == True:
        cartoonized = cartoonize(frame, 8)
        cv.imshow("Frame", cartoonized)
        # outCap.write(cartoonized)
        if cv.waitKey(26) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
outCap.release()
cv.destroyAllWindows()


#cartoonized = cartoonize(img, 8)

#cv.imshow("Input", img)
#cv.imshow("Output", cartoonized)
#cv.imwrite("cartoon.jpg", cartoonized)
# cv.waitKey(0)
