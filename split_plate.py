import numpy as np
import matplotlib.pyplot as plt
import cv2 
import math


def split_plate(plate):
    # img = cv2.imread('C:/Users/Botta/Downloads/label1.png',0)
    img=plate
    split_index=0
    s=img.shape
    r=int(s[0])
    c=int(s[1])
    num_labels, labels_im = cv2.connectedComponents(img)



    for col in range(math.ceil(c/2),c-1):
        index=1
        for row in range(0,r-1):
            if(img[row,col-1] != 0 or img[row,col-2] != 0 or img[row,col-3] != 0):
                index=0
                break
            if(img[row,col+1] != 0 or img[row,col+2] != 0 or img[row,col+3] != 0):
                index=0
                break
        if(index==1):
            split_index=col
            break
    charImg = np.zeros((r,col-split_index)) 
    charImg = img[0:r, split_index:c]
    #charImg = cv2.GaussianBlur(charImg,(1,1),1)
    # plt.figure()
    # plt.imshow(charImg,'gray')
    # plt.show()

    numberImg = np.zeros((r,split_index)) 
    numberImg = img[0:r, 0:split_index]
    # no_labels, labels, statistics, centers_cord = cv2.connectedComponentsWithStats(numberImg,4,cv2.CV_32S)
    # print(no_labels)
    # plt.figure()
    # plt.imshow(numberImg,'gray')
    # plt.show()
    
    return numberImg,charImg






