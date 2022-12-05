import cv2 as cv

input_filename = "../../assets/ifal.png"
img = cv.imread(input_filename)

if img is None:
    print("Impossível ler a imagem")


def edge_mask(img, line_size, blur_value):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray_blur = cv.medianBlur(gray, blur_value)
    edges = cv.adaptiveThreshold(
        gray_blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, line_size, blur_value)
    return edges


line_size = 3
blur_value = 3

edges = edge_mask(img, line_size, blur_value)

output_filename = "cartoon.jpg"
cv.imwrite(output_filename, edges)
cv.imshow("Sketch cartoon binary", edges)
cv.waitKey(0)
cv.destroyAllWindows()
