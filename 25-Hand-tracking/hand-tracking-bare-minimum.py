import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0)
# capturing video from the first camera

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# starting values of current and previous time
pTime = 0
cTime = 0


while True : 
    success, img = cap.read()
    imgRGB = cv.cvtColor(img , cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    # extracting multiple hands ( to check if there are multiple hands )
    print(results.multi_hand_landmarks)

    if(results.multi_hand_landmarks) : 
        # getting the coordinates of all the hands
        for handlms in results.multi_hand_landmarks :
            for id ,lm in enumerate(handlms.landmark) : 
                # print(id , lm)
                h,w,c = img.shape
                cx , cy = int(lm.x*w) , int(lm.y*h)
                print(id, cx , cy)


                # detecting the landmarks which is at the bottom of the palm ( it has the id of 0 )
                if(id==0) :     
                    # creating a circle on that coordinate
                    cv.circle(img , (cx , cy) , 25 , (255 , 0,255) , cv.FILLED)
            
            # drawing the hand 
            mpDraw.draw_landmarks(img , handlms , mpHands.HAND_CONNECTIONS) 
            


    # calculating the fps
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    # displaying the fps on the screen
    cv.putText(img , str(int(fps)) , (10,70) , cv.FONT_HERSHEY_PLAIN, 3 , (255 , 0 , 255) , thickness= 3)

    cv.imshow('Image' , img)
    cv.waitKey(1)
