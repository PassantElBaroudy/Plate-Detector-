from split_plate import *
def numANDchar(final_img1):
    number_img,char_img=split_plate(final_img1) #split the image into characters image and numbers image
    num_numbers,_,_,_=cv2.connectedComponentsWithStats(np.uint8(number_img), 4, cv2.CV_32S) #return the number of digits
    num_charc,_,_,_=cv2.connectedComponentsWithStats(np.uint8(char_img), 4, cv2.CV_32S)   #return the number of characters
    return num_numbers-1,num_charc-1  #minus one because we don't want to count the background as an object
