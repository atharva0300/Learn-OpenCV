import cv2 as cv

# importing the numpy package
import numpy as np

img = cv.imread('images/dog2.jpeg')
# reading an image from the file

# creating a blank image
blank = np.zeros((500 ,500 , 3) , dtype='uint8')
# creating a numpy array filled with zeros
# (500 , 500 , 3) => width,length and height of the blank image
# uint8 is the datatype of the image

cv.imshow('Blank' , blank)

# filling color in the blank image
blank[:] = 0,255,0
# selecting all the cells of the blank numpy array and filling it with 0,255,0 => green s

cv.imshow('Green' , blank)

# coloring a range of pixels
blank[200:300 , 300:400] = 0,0,255
cv.imshow('Red' , blank)

# Drawing a rectangle using cv.rectangle
cv.rectangle(blank , (0,0) , (250 , 250) , (0,255,0) , thickness=2)
# blank => passing the image to draw on to
# (0,0) => starting point
# (250 , 250) => point which is diagonally opposite to the starting point ( the ending point ) 
# (0,255,0) => color value  
# thickness = 2 => setting the thickness of the rectangle to 2

# displaying the rectangle
cv.imshow('Retangle' , blank)


cv.waitKey(20000)
