import cv2 as cv
# importing the cv2 module as cv 

# reading an image 
img = cv.imread('images/cat2.jpeg')

# displaying the image 
cv.imshow('cat' , img);

# delay, waits for a time ( in milliseconds )
# then closes the window
cv.waitKey(30000)
