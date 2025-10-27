# <-- Assignment 1 -->
# 1. Load image
# 2. Grayscale image
# 3. Show image
# 4. Save image
# desc: take file path from user in input and then grayscale that image and then ask they want to show or save image and if they want to save then ask filename to the user

import cv2 as cv

file_path = input("Enter file path : ")
image = cv.imread(file_path)
if image is not None:
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    if gray is not None:
        val = int(input("What you want \n 1.Show image \n 2. Save image\nEnter value from above: "))
        if val==1:
            cv.imshow("GrayScale Image",gray)
            cv.waitKey(0)
            cv.destroyAllWindows()
        elif val ==2:
            save_path = input("Enter file save name : ")
            save = cv.imwrite(save_path,gray)
            if save :
                print("Image saved successfully")
            else:
                print("Error : Image not saved")
        else:
            print("Selected invalid input")
    else:
        print("Error: Image not converted")
else:
    print("Error: Please provide correct image")