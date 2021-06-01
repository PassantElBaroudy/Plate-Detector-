from split_plate import *
def numANDchar(final_img1):
    number_img,char_img=split_plate(final_img1)
    num_numbers,_,_,_=cv2.connectedComponentsWithStats(np.uint8(number_img), 4, cv2.CV_32S)
    num_charc,_,_,_=cv2.connectedComponentsWithStats(np.uint8(char_img), 4, cv2.CV_32S)
    return num_numbers-1,num_charc-1