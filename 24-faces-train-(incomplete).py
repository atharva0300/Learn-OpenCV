import os 
import cv2 as cv
import numpy as np

people = ['modi' , 'trump' , 'netanyahu']
# creatin a list of people

DIR = r'/home/atharva007/Python/OpenCV-Learning/images/leaders/train'

# the training set will contain 2 lists
features = []
labels = []
# for every face, there will be a correcponding label

haar_cascade = cv.CascadeClassifier('haar_face.xml')


def create_train() :
    for person in people : 
        path = os.path.join(DIR , person)
        # joining the path

        # creating a label variable
        label = people.index(person)

        for img in os.listdir(path) : 
            img_path = os.path.join(path , img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array , cv.COLOR_BGR2GRAY)


            faces_rect = haar_cascade.detectMultiScale(gray , scaleFactor = 1.1 , minNeighbors = 4)

            for (x,y,w,h) in faces_rect :
                faces_roi = gray[y:y+h , x:x+w]
                features.append(faces_roi)
                labels.append(label)



create_train()

print('Training done')

fetures = np.array(features , dtype = 'object')
labels = np.array(labels)


print(f'Length of the features : {len(features)}')
print(f'Length of the labels : {len(labels)}')


face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features , labels)

np.save('features.npy' , features)
np.save('labels.npy' , labels)
