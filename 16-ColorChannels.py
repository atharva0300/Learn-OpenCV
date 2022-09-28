import cv2 as cv
import numpy as np

img = cv.imread('images/nature2.jpeg')
cv.imshow('Image' , img)

# splitting the image colors 
# getting the indovodual bgr colors
b,g,r = cv.split(img)

cv.imshow('blue' , b)
cv.imshow('green'  ,g)
cv.imshow('red' , r)

# parts of the image where red color is present is show more whiter.
# same for blue and green color images

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merging these color channels together
merged = cv.merge([b,g,r])
# passing a list of the bgr color channels
cv.imshow('merged' , merged)

# creating a blank image 
blank = np.zeros(img.shape[:2] , dtype=  'uint8')
# img.shape[:2] => getting the first 2 values of the img

blue = cv.merge([b , blank , blank])
green  = cv.merge([blank , g , blank])
red = cv.merge([blank , blank , r])

cv.imshow('blue 2' , blue)
cv.imshow('green 2'  ,green)
cv.imshow('red 2' , red)


cv.waitKey(20000)