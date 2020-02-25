import cv2
#import os
#import re
import sys

def eye_mosaic(file):

    face_cascade_path = 'haarcascade_frontalface_alt.xml'
    eye_cascade_path = 'haarcascade_eye.xml'

    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

    img = cv2.imread(file)
    imgConvertedGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Convert colors to gray as to make them more recognisable objects.
    faces = face_cascade.detectMultiScale(
        imgConvertedGrey,
        scaleFactor = 1.11, #scaleFactor is the number of test cases that system checks it is correct object
        minNeighbors = 5,   #negiboring objects will be erases there is redundancy
        )

    ratio = 0.035 

    #minSize for profile picture approximatey is 80X80, but can be varied.
    eyes = eye_cascade.detectMultiScale(imgConvertedGrey, scaleFactor=1.1,minNeighbors=12,minSize=(80,80))
    for (x, y, w, h) in eyes:
        small = cv2.resize(img[y: y + h, x: x + w], None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST) #This will turn eyes pixel into mosaic
        img[y: y + h, x: x + w] = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
    
    return img
    
img = eye_mosaic("download-3.png")
cv2.imwrite('./mosaic.png',img)

    
