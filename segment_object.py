import numpy as np
import matplotlib.pyplot as plt
import cv2
import math

def segment_object(img):
    #img = cv2.imread('C:/Users/dell/Desktop/Image Project/image 7.jpg')
    imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
    contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE , cv2.CHAIN_APPROX_NONE)
    #image_copy = img.copy()
    sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
    for (i, c) in enumerate(sorted_contours):
            #approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
                #cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
            #x = approx.ravel()[0]
            #y = approx.ravel()[1] - 5
            #if len(approx) == 4 :
            x, y, w, h = cv2.boundingRect(c)
            q = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
            if w > 100 :
                ROI = img[y:y + h, x:x + w];
                cv2.imshow('image', ROI)
                cv2.waitKey()
    return (ROI)