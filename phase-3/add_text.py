import cv2 as cv

image = cv.imread("phase-3/roadmap-3.png")
h,w=image.shape[:2]
if image is not None:
    text_image=cv.putText(image,"Hello world",(w//2,h//2),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,255,),thickness=1)
    cv.imshow('Text image',text_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
