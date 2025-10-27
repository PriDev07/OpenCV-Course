import cv2 as cv

image = cv.imread("phase-3/roadmap-3.png")
h,w=image.shape[:2]
if image is not None:
    circle_image=cv.circle(image,(w//2,h//2),100,color=(0,0,255),thickness=10)
    cv.imshow("Circle Image",circle_image)
    cv.waitKey(0)
    cv.destroyAllWindows()