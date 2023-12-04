import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'imageAttendance'
images = []
classNames = []
#we are grabbing the images of this folder
myList = os.listdir(path)
print(myList)
#for class in my list
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    #we are grabbing the first element
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

#we are going to read all the lines of data
#you can link this func to a database below
def markAttendance(name):
    pass
    with open("Attendance.csv","r+") as f:
        myDataList = f.readlines()
        print(myDataList)
        #we are putting all the names we find in this list
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            #we are fixing the first element of our entry
            nameList.append(entry[0])
        #once we have all the names we are going to check whether the new name is there or not
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')




encodeListKnown = findEncodings(images)
print("Encoding Complete")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    #we are reducing the size of the image
    imgSmall = cv2.resize(img,(0,0),None,0.25,0.25)
    #we have to convert the image above to rgb
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgSmall)
    encodesCurFrame = face_recognition.face_encodings(imgSmall, facesCurFrame)

    #we are finding the matches
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDis)
        #we get the index of the match below to appropriate them
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            #find the location of the face
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)

    cv2.imshow('Webcam',img)
    cv2.waitKey(1)








