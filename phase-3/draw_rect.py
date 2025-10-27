import cv2 as cv

image = cv.imread("phase-3/roadmap-3.png")

if image is not None:
    rect_image=cv.rectangle(image,(1500,1500),(500,500),color=(0,0,255),thickness=5)
    cv.imshow('Rectangle image',rect_image)
    cv.waitKey(0)
    cv.destroyAllWindows()