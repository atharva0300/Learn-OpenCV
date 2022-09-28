import cv2 as cv


img = cv.imread('images/dog2.jpeg')
cv.imshow('Image' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

# Simple thresholding
threshold , thresh = cv.threshold(gray , 150 , 255 , cv.THRESH_BINARY )
# 150 => condition = if the value is greater than 150 then
# 255 => if the above condition is satified, then set the pixel to 255 else set it to 0
# cv.THRESH_BINARY = the thresh algo
cv.imshow('Simple Thresholding' , thresh)

# creating an inverse threshold of an image
threshold , thresh_inv = cv.threshold(gray , 150 , 255 , cv.THRESH_BINARY_INV)
cv.imshow('Simple Inverse Thresholding' , thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_MEAN_C , cv.THRESH_BINARY , 11 ,3)
# cv.ADAPTIVR_THRESH_MEAN_C => setting different threshold value for each pixel
# dsize : 11 
# c : 3. increasing the c, decreases the white part. 
cv.imshow('Adaptive Thresholding' , adaptive_thresh)

adaptive_thresh = cv.adaptiveThreshold(gray , 255 , cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY , 11 ,3)
cv.imshow('Gaussian Adaptive Thresholding' , adaptive_thresh)


cv.waitKey(20000)
