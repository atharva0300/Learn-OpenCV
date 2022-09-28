import cv2 as cv
import numpy as np

img = cv.imread('images/dog2.jpeg')

cv.imshow('Dog' , img)

# converting the image to grayscale
gray = cv.cvtColor(img  , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

blur = cv.GaussianBlur(gray , (5,5)  , cv.BORDER_DEFAULT)
cv.imshow('Blur' , blur)

# canny image
canny = cv.Canny(img , 125 , 175)
# 125 and 175 are threshold values

cv.imshow('Canny Edges' , canny)

canny = cv.Canny(blur , 125 , 175)
# 125 and 175 are threshold values

cv.imshow('Blur Canny Edges' , canny)

ret , thresh = cv.threshold(gray , 125 , 255 , cv.THRESH_BINARY)



# finding contours 
contours, hierarchies = cv.findContours(canny , cv.RETR_LIST , cv.CHAIN_APPROX_NONE)
# cv.RETR_LIST => to list all the contours of the image 
# cv.CHAIN_APPROX_NONE => contour approximation method

# contours => a python list that contains the coordinates of the contours
# hierarchies => teh hierarchical representation of the contouts

print(f'{len(contours)} contours found!')


contours, hierarchies = cv.findContours(thresh , cv.RETR_LIST , cv.CHAIN_APPROX_NONE)

print(f'{len(contours)} contours found!')

blank = np.zeros((500 , 500 , 3) , dtype = 'uint8')

cv.drawContours(blank , contours , -1  , (0,0,255) , thickness=2)
# blank => the image to draw onto
# contours => displaying the contours 
# -1 => drawing all the contours
# 0,0,255 => the color
# thickness = 2 => the thickness of the contour
cv.imshow('Contours Drawn' , blank)

cv.drawContours(canny , contours , -1  , (0,0,255) , thickness=2)
cv.imshow('Contours Drawn 2' , canny)

cv.drawContours(blur , contours , -1  , (0,0,255) , thickness=2)
# blank => the image to draw onto
# contours => displaying the contours 
# -1 => drawing all the contours
# 0,0,255 => the color
# thickness = 2 => the thickness of the contour
cv.imshow('Contours Drawn blur' , blur)





cv.waitKey(20000)