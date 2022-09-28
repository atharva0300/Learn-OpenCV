import cv2 as cv
import numpy as np

img = cv.imread('images/cat2.jpeg')
cv.imshow('Image' , img)

blank = np.zeros(img.shape[:2] , dtype = 'uint8')
cv.imshow('Blank Image' , blank)


rectangle = cv.rectangle(blank.copy() , (30 , 30) , (370 , 370) , 255 , -1)
circle = cv.circle(blank.copy() , (200 , 200) , 200 , 255 , -1)

# creating a mask
mask = cv.circle(blank , (img.shape[1]//2 , img.shape[0]//2) , 100 , 255 , -1 )
cv.imshow('Mask' , mask)

masked = cv.bitwise_and(img , img , mask = mask)
cv.imshow('Masked Image' , masked)


cv.imshow('Rectangle' , rectangle)
cv.imshow('Circle' , circle)

weird_shape = cv.bitwise_and(circle , rectangle)
cv.imshow('Weird shape' , weird_shape)

masked = cv.bitwise_and(img , img , mask = weird_shape)
cv.imshow('Masked Image 2' , masked)




cv.waitKey(20000)
