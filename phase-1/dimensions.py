import cv2 as cv

image = cv.imread("image/ss1.png")
if image is not None:
    h, w, c = image.shape
    print(f"Image loaded:\nheight: {h}\nwidth: {w}\nchannel: {c}")
else:
    print("Image not found")