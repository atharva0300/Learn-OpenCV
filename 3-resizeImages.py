import cv2 as cv

img = cv.imread('images/cat1.jpeg')

def rescaleFrame(frame, scale = 2): 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width , height)

    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)

cv.imshow('Cat' , rescaleFrame(img)) 
# passing the img to the resclae function to get the sclaed image 
# passing the returned image to the imshow function to display the image

cv.waitKey(20000)