import cv2 as cv
import matplotlib.pyplot as plt

# color space => a space of color ( like BGR , RGB , HSV etc )

# converting  the bgr image to grayscaele
img = cv.imread('images/cat2.jpeg')
cv.imshow('Original Image', img )

gray = cv.cvtColor(img  , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

# converting bgr to hsv 
# hdv => hue , saturation value
hsv = cv.cvtColor(img , cv.COLOR_BGR2HSV_FULL)
cv.imshow('HSV' , hsv)

# converting from bgr to l*a*b
lab =cv.cvtColor(img , cv.COLOR_BGR2LAB)
cv.imshow('LAB' , lab)

# opencv reads the image in BGR format ( blue green red )
plt.imshow(img)
plt.show()
# this dislays the RGB image instead of BGR image, so the original image's color gets inverted



# we convert the BGR image to RGB image in openCV
rgb = cv.cvtColor(img , cv.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()

# converting HSV to BGR
hsv_bgr = cv.cvtColor(hsv , cv.COLOR_HSV2BGR_FULL)
cv.imshow('hsv to bgr' , hsv_bgr)

# lab to bgr
lab_bgr = cv.cvtColor(lab , cv.COLOR_LAB2BGR)
cv.imshow('lab to bgr' , lab_bgr)

# converting grayscale to lab image,. there is no direct method 
# convert the grayscale to bgr, then the bgr image to labs

cv.waitKey(20000)