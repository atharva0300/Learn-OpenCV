import cv2 as cv

video = cv.VideoCapture('video/cat.mp4')

# rescale function 
def rescaleFrame(frame , xscale = 0.25 , yscale = 0.25) : 
    width = int(frame.shape[1] * xscale)
    height = int(frame.shape[0] * yscale)

    dimensions  = (width ,height)
    # creating a tuple of the modified width and the modified height

    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)
    # passing the frame and the final dimension


while True : 
    isTrue , frame = video.read()
    # extracting the frame and the isTrue value ( ie => if the frame is there or not )

    # getting the resized frame
    frame_resized = rescaleFrame(frame)

    # displaying the resized frame
    cv.imshow('Video' , frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d') :
        break


video.release()
cv.destroyAllWindows()
