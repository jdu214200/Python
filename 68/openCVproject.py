import cv2 as cv

myImage = cv.imread('Picture/JapanMap.png')

print(myImage.shape)

cv.imshow('JAPAN', myImage)

cv.waitKey(0)

import cv2 as cv

myImage2 = cv.imread('Picture/CentralAsianMap.jpg')
print(myImage2.shape)
cv.imshow('Markaziy osiyo', myImage2)
cv.waitKey(0)

h, w = myImage2.shape[:2]
heigth, width = int(h/2), int(w/2)

myImageResized = cv.resize(myImage2, (width, heigth))

cv.imshow('Japan', myImage2)
cv.waitKey(0)