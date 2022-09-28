import cv2 as cv

img = cv.imread('images/nature2.jpeg')
cv.imshow('Nature' , img)

# converting to grayScale
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)


# blurring the image
blur = cv.GaussianBlur(img , (3,3) , cv.BORDER_DEFAULT)
# 3,3 => the kernel size ( highher the kernel size, higher the blur )
# cv.BORDER_DEFAULT => the blurring algorithm
cv.imshow('Blur' , blur)


# edge cascading
canny = cv.Canny(img , 125 ,175)
# 125 and 175 are the threshold value
cv.imshow('Canny Edges' , canny)

# dilating the image
dilated = cv.dilate(canny , (3,3) , iterations = 1)
# 3,3 => the kernel size ( highher the kernel size, higher the dilation )
# iterations => the iterations required for dilations
cv.imshow('Dilated' , dilated)

# eroding
eroded = cv.erode(dilated , (3,3) , iterations = 1)
# 3,3 => the kernel size ( highher the kernel size, higher the dilation )
# iterations => the iterations required for dilations
cv.imshow('Eroded' , eroded)

# resize
resized = cv.resize(img , (500 , 500))
cv.imshow('Resized'  ,resized)

resized = cv.resize(img , (500 , 500) , interpolation=cv.INTER_AREA)
cv.imshow('Resized2'  ,resized)

resized = cv.resize(img , (500 , 500) , interpolation=cv.INTER_CUBIC)
cv.imshow('Resized3'  ,resized)

# cropping
cropped = img[50:200 , 200:400]
# seleting the range ( part ) of the image
cv.imshow('Cropped' , cropped)


cv.waitKey(20000)
