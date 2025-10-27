import cv2 as cv

image = cv.imread("image/ss1.png")
if image is not None:
    cv.imshow('Image',image)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("image not found")