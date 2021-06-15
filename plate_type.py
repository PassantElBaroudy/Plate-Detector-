# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 12:27:14 2021

@author: My Lap
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 26 23:08:03 2021
@author: My Lap
"""
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def plate_type(path):
    im = cv2.imread(path,1)
    RGB_img = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    dst = cv2.fastNlMeansDenoisingColored(RGB_img, None, 10, 10, 10, 15)
    bigger_denoised = cv2.resize(dst, (2000, 1000))
    crop_img = bigger_denoised[130:200,950:1000]
    plt.imshow(crop_img)
# Make into Numpy array
    na = np.array(crop_img)

# Arrange all pixels into a tall column of 3 RGB values and find unique rows (colours)
    colours, counts = np.unique(na.reshape(-1,3), axis=0, return_counts=1)
    x=np.sum(colours,axis=0)/np.size(colours,0)
    x = x.astype(int)
    #print(x)     
    if ((x[0]>=128 and x[0]<=255) and (x[1]>=30 and x[1]<=100) and (x[2]>=30 and x[2]<=122)):
         type="TransportationCar"
    elif (( x[0]>=25 and x[0]<=65) and ( x[1]>=25 and x[1]<=105) and ( x[2]>=112 and x[2]<=225)):
        type="PoliceCar"
    elif ((x[0]>=0 and x[0]<=127) and (x[1]>=84 and x[1]<=255) and (x[2]>=160 and x[2]<=255)):
        type="PrivateCar"
    elif ((x[0]>=205 and x[0]<=255) and (x[1]>=92 and x[1]<=165) and (x[2]>=0 and x[2]<=92)):
        type="Taxi"
    elif ((x[0]>=189 and x[0]<=255) and (x[1]>=183 and x[1]<=255) and (x[2]>=0 and x[2]<=107)):
        type="CustomsCar"
    elif ((x[0]>=60 and x[0]<=152) and (x[1]>=107 and x[1]<=251) and (x[2]>=47 and x[2]<=152)):
        type="PoliticalCar"
    elif ((x[0]>=139 and x[0]<=255) and (x[1]>=69 and x[1]<=218) and (x[2]>=19 and x[2]<=185)):
        type="CommercialCar" 
    else:
        type="NO TYPE"
       
    return type
  

#kind=plate_type('E:/4th CSE/2nd Term/Image processing/project/testorange.jpeg')  
#print (kind)
