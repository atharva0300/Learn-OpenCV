import cv2 as cv
import numpy as np

img = cv.imread('images/nature2.jpeg')
cv.imshow('Image' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)


# Laplacian method for edge detection
lap = cv.Laplacian(gray , cv.CV_64F)
# cv.64F => data depth
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian' , lap)

# Sobel method for edge detection  
sobelx = cv.Sobel(gray , cv.CV_64F , 1 , 0)
sobely = cv.Sobel(gray , cv.CV_64F , 0 , 1)

cv.imshow('Sobel X ' , sobelx)
cv.imshow('Sobel Y' , sobely)

# combining both the sobels
combined_sobel = cv.bitwise_or(sobelx , sobely)
cv.imshow('Combined Sobel'  , combined_sobel)

# canny edge detector
canny = cv.Canny(gray , 150 , 175)
cv.imshow('Canny' , canny)






cv.waitKey(20000)
