import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('images/dog1.jpeg')
cv.imshow('Dog' , img)

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)

# Grayscale image
gray_hist = cv.calcHist([gray] , [0] , None, [256] , [0,256])
# gray => the image of which to calculate the grayscale histogram of
# channels = 0 
# None => the mask is set to none here
# histSize = 256 => the size of the histogram
# ranges of all the pixel values = 0,256 

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

blank = np.zeros(img.shape[:2] , dtype = 'uint8')

# creating a mask
mask = cv.circle(blank , (img.shape[1]//2 , img.shape[0]//2) , 100 , 255 , -1 )
cv.imshow('Mask' , mask)

masked = cv.bitwise_and(img , img , mask = mask)
cv.imshow('Masked Image' , masked)

gray_hist = cv.calcHist([masked] , [0] , None, [256] , [0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# color histogram 
colors = ('b' , 'g' , 'r')
for i, col in enumerate(colors) : 
    hist = cv.calcHist([img] , [i] , None , [256] , [0,256])
    plt.plot(hist , color = col)
    plt.xlim([0 , 256])


plt.show()



cv.waitKey(20000)


