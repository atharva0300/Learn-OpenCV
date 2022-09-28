import cv2 as cv

img = cv.imread('images/dog2.jpeg')
cv.imshow('Image' , img)

# Averaging
average = cv.blur(img  , (3,3))
cv.imshow('average blur' , average)
# highher the kernel size , higher the blur
# the average blur is caluclated by taking the AVERAGE of the surrounding intensities of the targeted pixel

# gaussian blur
gauss = cv.GaussianBlur(img  ,(3,3) , 0)
# 0 => standard deviation
cv.imshow('Gaussian blur' , gauss)

# median blur
median = cv.medianBlur(img , 3)
# the median blur is calculated by taking the MEDIAN of the surrouding intensities of the targeted pixel
# 3 => is a 3*3 kernel size
cv.imshow('Median Blur' , median)


# Bilateral blurring
# applies blurring but, the edges can be retained
bilateral = cv.bilateralFilter(img ,  5 , 35 , 25)
# d size = 5 
# sigmaCOlor = 35 => more the value, more colors are considered
# sigmaSpace = 25 => how many pixels far away from the targeted pixel do you want to consider to calculate the bilateral blur
cv.imshow('Bilateral' , bilateral)

cv.waitKey(20000)