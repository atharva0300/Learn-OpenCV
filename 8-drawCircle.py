import cv2 as cv
import numpy as np

blank = np.zeros((500 , 500 , 3) , dtype ='uint8')

cv.circle(blank , (250 , 250), 40 , (0,0,255) , thickness=-1)
# draw => the image on which to draw onto
# (250 , 250) => the center coordinate of the circle
# 40 => the radius of the circle
# (0,0,255) => the color ( red )
# thickness => the thickness of the circle. setting the thickness to -1, fills the color

# displaying the circle
cv.imshow('Circle' , blank)


cv.waitKey(20000)