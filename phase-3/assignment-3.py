# <-- Assignment 3 -->
# 1. Load image
# 2. Ask for which type of draw(i.e. circle, line, rectangle, text)
# 3. ask coordinates of center or where they want to save
# 4. ask save or show
# 5. if save selected then ask the saving file name
# 6. if show selected then show that new image
# description : firslt load image by asking the user file location and then ask what they want to draw and then ask them coordinates where they want to add and then want to show or save, if save selected then ask output file name and if show selected then show the image.

import cv2 as cv

file_path = input("Enter file path: ")
image = cv.imread(file_path)
h,w=image.shape[:2]
if image is not None:
    inp = int(input("Enter what you want : \n1. Line \n2. Circle \n3. Text \n4. rectangle"))
    if inp==1:
        coordinates_x = int(input("Enter X: "))
        coordinates_y = int(input("Enter Y: "))
        img_lined=cv.line(image,(0,0),(coordinates_x,coordinates_y),color=(255,120,60),thickness=100)
        cv.imshow('Lined image',img_lined)
        cv.waitKey(0)
        cv.destroyAllWindows()
    elif inp ==2:
        rad = int(input("enter Radius: "))
        circle_image=cv.circle(image,(w//2,h//2),100,color=(0,0,255),thickness=10)
        cv.imshow("Circle Image",circle_image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    elif inp ==3:
        txt = input("enter text: ")
        text_image=cv.putText(image,txt,(w//2,h//2),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,0,255,),thickness=1)
        cv.imshow('Text image',text_image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    elif inp==4:
        start_coordinates_x = int(input("Enter X: "))
        start_coordinates_y = int(input("Enter Y: "))
        end_coordinates_x = int(input("Enter X: "))
        end_coordinates_y = int(input("Enter Y: "))
        rect_image=cv.rectangle(image,(start_coordinates_x,start_coordinates_y),(end_coordinates_x,end_coordinates_y),color=(0,0,255),thickness=5)
        cv.imshow('Rectangle image',rect_image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        print("Error : Wrong input")
else:
    print("Error: Image not found")

