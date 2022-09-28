import cv2 as cv

video = cv.VideoCapture('video/dog.mp4');
# passing the path of the video
# passing teh path as => 0 will reference the webcam 
#       => 1 first cam
#       => 2 second cam

# creating a loop
while True : 
    isTrue, frame = video.read()
    #  returns the frame and returns if that frame was captured successfully or not
    cv.imshow('Video' , frame)
    # displaying the video frame by frame

    # if the time exceeds, then break the loop ( ie => stop displaying the video )
    if cv.waitKey(20) & 0xFF==ord('d') :
        break

    # We get an error after the video completes and stops playing. because there is not frame after the last frame 
    # of the video, so, the value of frame is undefined.
    # so it gives an error ( its normal )

video.release()
# 

cv.destroyAllWindows()
# destroys all the windows ( frames ) created, after the windows as exited
