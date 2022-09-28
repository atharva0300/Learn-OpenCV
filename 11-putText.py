import cv2 as cv
import numpy as np

blank = np.zeros((500 , 500 , 3) , dtype = 'uint8')

# write text on image
cv.putText(blank  , 'Hello Atharva' , (150 , 255) , cv.FONT_HERSHEY_COMPLEX , 1.0 , (0,255,0) , thickness=2)
# blank = > the image to draw onto
# Hello Atharva => the text to write
# 255 , 255 => The starting coordinate of the text
# cv.FONT_HERSHEY_COMPLEX => the font provided by cv
# 1.0 => scale 
# (0,255,0 ) => color of the text
# thickness=2 => the thickness
 
cv.imshow('Text' , blank)

cv.waitKey(20000)