import cv2 as cv
import numpy as np

blank = np.zeros((500 , 500 , 3) , dtype = 'uint8')

# Drawing a rectangle using cv.rectangle
cv.rectangle(blank , (0,0) , (250 , 250) , (0,255,0) , thickness=2)
cv.imshow('Retangle' , blank)


cv.circle(blank , (250 , 250), 40 , (0,0,255) , thickness=-1)
cv.imshow('Circle' , blank)

cv.line(blank , (0,0) , (250 , 250) , (255 , 255 , 255) , thickness = 1)
cv.imshow('Line' , blank)


cv.waitKey(20000)