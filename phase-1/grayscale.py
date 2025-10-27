import cv2 as cv

image = cv.imread("output.png")

if image is not None:
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("Grayscale image", gray)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Image not found")