import cv2 as cv

video = cv.VideoCapture(0)
# passing 0 means taking the video input from a webcam

# change the resolution of the image
def changeRes(width , height) :
    # change res works for Webcam and not for standalone files ( the vidoe files that already exists )
    video.set(3 , width)
    video.set(4 , height)


while True : 
    isTrue , frame = video.read()

    changeRes(2 , 2)

    cv.imshow('Video' , frame)

    if cv.waitKey(20) & 0xFF==ord('d') :
        break

video.release()
cv.destroyAllWindows()
