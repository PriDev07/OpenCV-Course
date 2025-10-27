import cv2 as cv

image = cv.imread('phase2/roadmap-2.png')

if image is not None:
    flipped_hor = cv.flip(image,1) # For flipping horizontally
    flipped_ver = cv.flip(image,0) # For flipping vertical
    flipped_both = cv.flip(image,-1) # For flipping from both horizontal and vertical
    cv.imshow("Flipped  Window",flipped_both)
    cv.waitKey(0)
    cv.destroyAllWindows()