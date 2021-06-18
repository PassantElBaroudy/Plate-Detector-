import easyocr


#from PIL import Image




def easyOcr(number_img,char_img):
    
    #img = cv2.imread(imgPath)
    reader = easyocr.Reader(['ar']) # need to run only once to load model into memory
    #final_img,num_objects,dims,centers=plate_enhancement(img)
    #number_img,char_img=split_plate(final_img)
    #plt.imshow(number_img)
    #plt.imshow(char_img)
    chars = reader.readtext(char_img)
    numbers = reader.readtext(number_img)
    
    chars = chars[0][1].replace(" ","")
    numbers = numbers[0][1].replace(" ","")
    
    return numbers,chars










# for i in range(1,num_objects):
#     y=dims[i,cv2.CC_STAT_HEIGHT]
#     x= dims[i,cv2.CC_STAT_WIDTH]
#     left=dims[i,cv2.CC_STAT_LEFT]
#     top=dims[i,cv2.CC_STAT_TOP]   
    

    
     
#     n1 = np.zeros((final_img.shape[0],final_img.shape[1]))
#     n = np.zeros((x,y)) 
    
#     n = final_img[ top : y+top, left : x+left] 
    
#     for i in range(n.shape[0]):
#         for j in range(n.shape[1]):
#             if n[i][j] == 255:
#                 n1[i+44][j+85]=255
                
#     n1 = n1.astype(np.uint8)

    
    
#     plt.imshow(n1,'gray')

    
#     result = reader.readtext(n1)
#     imageChar.append(result)
#     plt.figure()
#     plt.show()



# info = np.iinfo(data.dtype) # Get the information of the incoming image type
# data = data.astype(np.float64) / info.max # normalize the data to 0 - 1
# data = 255 * data # Now scale by 255
# img = data.astype(np.uint8)
# cv2.imshow("Window", img)



# plt.figure()
# plt.imshow(number_img,'gray')
# plt.show()
# plt.figure()
# plt.imshow(char_img,'gray')
# plt.show()
