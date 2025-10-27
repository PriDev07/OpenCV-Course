import cv2 as cv

image = cv.imread('phase-1/roadmap-1.png')

if image is not None:
    output = cv.imwrite('output.png',image)
    if output:
        print('Image added successfully')
    else:
        print('Image not added')
else:
    print('image not found')