import cv2 as cv

image = cv.imread('phase2/roadmap-2.png')

if image is not None:
    h,w = image.shape[:2]
    center = (w//2,h//2) # to get the center of the image
    M = cv.getRotationMatrix2D(center,180,1.0)
    rotated=cv.warpAffine(image,M,(w,h))
    cv.imshow('Rotated Image',rotated)
    cv.waitKey(0)
    cv.destroyAllWindows()