Modelgeneration.py [Model Generation]:
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
def getface(image):
    classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    face = classifier.detectMultiScale(grey, 1.3, 5)
    if face is ():
        return None
    image=image[face[0,0]:(face[0,0]+face[0,2]),face[0,1]:(face[0,1]+face[0,3])]
    image=cv2.resize(image,(200,200))
    return image
cap=cv2.VideoCapture(0)
count=0
while True:
    status, image=cap.read()
    if getface(image) is not None:
        count += 1
        face=getface(image)
        file_name_path = 'D://faces//image' + str(count) + '.jpg'
        cv2.imwrite(file_name_path, face)
        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        cv2.imshow('Face Cropper', face)
    if cv2.waitKey(1)==13 or count==100:
        break
cv2.destroyAllWindows()
cap.release()
data_path = 'd://faces//'

onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

# Create arrays for training data and labels
Training_Data, Labels = [], []

# Open training images in our datapath
# Create a numpy array for training data
for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)
# 
# Create a numpy array for both training data and labels
Labels = np.asarray(Labels, dtype=np.int32)
model=cv2.face_LBPHFaceRecognizer.create()
model.train(np.array(Training_Data), np.array(Labels))
print("Model trained successfully")
model.save('face_recognizer.xml')
