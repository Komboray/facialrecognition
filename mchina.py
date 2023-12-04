import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file('imageBasics/elon.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('imageBasics/elon2.jpeg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

#THE FIRST FACE DETECTION
#sending in an image of the first element
faceLoc = face_recognition.face_locations(imgElon)[0]
#encoding the face that we have detected
encodeElon = face_recognition.face_encodings(imgElon)[0]
#we are detecting the faces with a square from faceLoc which has the dimensions then we are building a square face on the detected faces with purple
cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2 )

#THE SECOND FACE DETECTION
#we are comparing the two faces
faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLoc[3], faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

#we are comparing the encoded image
results = face_recognition.compare_faces([encodeElon],encodeTest)
#WE ARE GOING TO FIND THE BEST MATCH
faceDis = face_recognition.face_distance([encodeElon],encodeTest)
#the below evaluation
print(results, faceDis)

#display on the actual image
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


cv2.imshow('Elon Musk',imgElon)
cv2.imshow('Elon Test',imgTest)
cv2.waitKey(0)
