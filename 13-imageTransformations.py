import cv2 as cv
import numpy as np

img = cv.imread('images/cat2.jpeg')

cv.imshow('Cat' , img)

# translating an image
def translate(img , x , y) : 
    # creating a translation matrix
    transMat = np.float32([[1,0,x] , [0,1,y]])

    dimensions = (img.shape[1] , img.shape[0])
    # getting the dimensions of the image

    return cv.warpAffine(img , transMat , dimensions)
    # img => the image to translate
    # transMat => the translation to give
    # dimentions 


# +x => right 
# -x => left
# +y => down 
# -y => up

translated = translate(img , 100 , 100)
# shofting the image to the right and down
cv.imshow('Translated'  , translated)

# rotation
def rotate(img , angle , rotPoint = None) :
    (height , width ) = img.shape[:2]

    if(rotPoint==None ) : 
        # if the rotating point is None 
        # then assuming to rotate around the center
        rotPoint = (width//2 , height//2)

    rotMat =cv.getRotationMatrix2D(rotPoint , angle , 1.0)
    dimensions = (width , height)

    return cv.warpAffine(img , rotMat , dimensions)

# invoking the rotate function
rotated = rotate(img , 45)

# displaying the rotated image
cv.imshow('Rotate' ,  rotated)  

rotated_rotated = rotate(rotated , 45)
cv.imshow('Rotated Rotated' , rotated_rotated)


# resizing
resized = cv.resize(img , (500 , 500) , interpolation=cv.INTER_CUBIC)
cv.imshow('Resized'  , resized)

# flipping an image
flip = cv.flip(img , 0)
# flipcode => 
#   0 => flipping the image vertically 
#   1 => flip the image horizontally
#   -1 => flip the image both horizontally and vertically 
cv.imshow('Flip' , flip)

flip = cv.flip(img , -1)
cv.imshow('Flip -1' , flip)


# cropping
cropped1 = img[200:400 , 200:300]
cv.imshow('crop1' , cropped1)



cv.waitKey(20000)
