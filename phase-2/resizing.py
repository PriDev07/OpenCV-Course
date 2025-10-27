import cv2 as cv

image = cv.imread('phase2/roadmap-2.png')
#resize(src,(change_width,change_height))
if image is not None:
    resized = cv.resize(image,(400,400))
    cv.imshow('Original image',image)
    cv.imshow('Resized Image',resized)
    cv.imwrite('resized_output.png',resized)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print('Image not found')