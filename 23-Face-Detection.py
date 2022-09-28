import cv2 as cv

# face detection => detects the presence of a face 
# face recognition => recognizes whose face is it

# we use classifiers
# openCV has inbuilt classifiers called as HaarCascades

img = cv.imread('images/people/people5.jpeg')
cv.imshow('Image' , img)

# converting the image to grayscale image
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale' , gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray , scaleFactor = 1.1 , minNeighbors = 5)
# minNeighbors => identify 5 faces at max
# modifying the scaleFactor and minNeighbors continuously, and then finally you will find a value, where the faces identification
# is perfect

print(f'Number of faces found : {len(faces_rect)}')

for (x,y,w,h) in faces_rect : 
    cv.rectangle(img  , (x,y) , (x+w , y+h) ,(0,255,0) , thickness = 2)

cv.imshow('Detected faces' , img)


cv.waitKey(20000)

