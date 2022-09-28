from curses.textpad import rectangle
import cv2 as cv
import numpy as np

# bitwise operators operate in a binary manner
# a pixel is turned off if it has a value of 0
# it is turned on, if it has a value of 1 

blank = np.zeros((400 , 400) , dtype= 'uint8')
rectangle = cv.rectangle(blank.copy() , (30 , 30) , (370 , 370) , 255 , -1)
circle = cv.circle(blank.copy() , (200 , 200) , 200 , 255 , -1)

cv.imshow('Rectangle' , rectangle)
cv.imshow('Circle' , circle)

# bitwise AND
bitwise_and = cv.bitwise_and(rectangle , circle)
# returns the intersection of the 2 images
cv.imshow('bitwise and' , bitwise_and)

# bitwise_or
bitwise_or = cv.bitwise_or(rectangle , circle)
# returns the OR value of 2 images
cv.imshow('bitwise or' , bitwise_or)

# bitwise_xor
bitwise_xor = cv.bitwise_xor(rectangle , circle)
# returns the NON-INTERSECTING regions 
cv.imshow('bitwise_xor' , bitwise_xor)

# bitwise_not
bitwise_not = cv.bitwise_not(rectangle)
# inverts the image
cv.imshow('bitwise_not' , bitwise_not)

circle_not = cv.bitwise_not(circle)
cv.imshow('Circle not' , circle_not)


cv.waitKey(20000)