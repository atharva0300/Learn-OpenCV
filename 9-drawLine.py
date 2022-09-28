import cv2 as cv
import numpy as np

blank = np.zeros((500 , 500 , 3) , dtype = 'uint8')

cv.line(blank , (0,0) , (250 , 250) , (255 , 255 , 255) , thickness = 1)
# 0,0 => starting coordinate 
# 250 , 250 => ending coordinate
# 255 , 255 , 255 => color of the line
# thickness => thickness of the lines

# displaying the image
cv.imshow('Line' , blank)


cv.waitKey(20000)
