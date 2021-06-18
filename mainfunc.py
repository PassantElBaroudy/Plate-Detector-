from numpy.core.fromnumeric import resize
from plate_enhancement import *
from split_plate import *
from numANDchar import *
from plate_type import *
from Mohfza import *
from easyOcr import *
def mainfunc(path):
    
    img = cv2.imread(path)
    final_img,num_objects,dims,centers,final_img1=plate_enhancement(img)
    number_img,char_img=split_plate(final_img) #final_img without dilate
    numbers,chars=easyOcr(number_img,char_img)
    num_numbers,num_charc=numANDchar(final_img1) #final_img1 with
    GovName=Mohfza(num_numbers,num_charc,chars)
    carcolor=plate_type(path)

    return carcolor,GovName,chars,numbers
