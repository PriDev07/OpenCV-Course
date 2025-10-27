import cv2 as cv

image = cv.imread('phase2/roadmap-2.png')

if image is not None:
    cropped = image[100:1000,:1500] #image[startY:endY,startX,endX]
    cv.imshow('Cropped Image',cropped)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print('Image not found')
 