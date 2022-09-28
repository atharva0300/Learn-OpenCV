import cv2 as cv
import numpy as np

blank = np.zeros((500 , 500 , 3) , dtype = 'uint8')

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