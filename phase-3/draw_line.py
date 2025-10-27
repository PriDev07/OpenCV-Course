import cv2 as cv

image = cv.imread("phase-3/roadmap-3.png")

if image is not None:
    img_lined=cv.line(image,(0,0),(1000,1200),color=(255,120,60),thickness=100)
    cv.imshow('Lined image',img_lined)
    cv.waitKey(0)
    cv.destroyAllWindows()