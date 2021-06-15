# -*- coding: utf-8 -*-
"""
Created on Mon May 31 20:21:51 2021

@author: My Lap
"""
#from numANDchar import *
#from names import *
#from plate_enhancement import *

def Mohfza(NO_numbers,NO_chars,chars):
    #NO_numbers,NO_chars=numANDchar(path)
    #numbers,chars=easyOcr(path)
    if (NO_numbers==3 and NO_chars==3):
        Name="Cairo"       
    elif (NO_numbers==4 and NO_chars==2):
        Name="Giza"
    elif (chars[0]=="س" and NO_numbers==4 and NO_chars==3):
       Name="Alex"
    elif (chars[0]=="ط" and chars[1]=="د" and NO_numbers==4 and NO_chars==3):
       Name="Demiita"
    elif (chars[0]=="د" and NO_numbers==3 and NO_chars==3):
       Name="Dakahlia"
    elif (chars[0]=="ص" and NO_numbers==3 and NO_chars==3):
       Name="Aswan"
    elif (chars[0]=="ف" and NO_numbers==3 and NO_chars==3):
       Name="Fayoum"
    elif (chars[0]=="ن" and NO_numbers==3 and NO_chars==3):
       Name="ElMinya"
    else:
        Name="Other"
        
    return Name
    

#Name=Mohfza('E:/4th CSE/2nd Term/Image processing/project/testyellow.jpeg')
#print(Name)