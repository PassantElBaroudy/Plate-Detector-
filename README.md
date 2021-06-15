# Plate-Detector-

# Team Members:
1-Andrew Rafaat

2-Pavly Mario

3-Passant Mohamed 

4-Salah Adel

5-Youssef Rafaat

 # Requirements:
 

# Description:
•The project idea is to implement an image processing algorithm that aims to detect the vehicle plate’s type and its governorate in a given image and detect the characters and numbers in it , It also detects the car’s owner information ( Name ) and it detects the car’s modeland traffic violations .



# Implementation:
1-PlateType: This function takes the plate image then resize it and crop the image to get the upper part and apply some functions to get the pixels of the image and its values then 
get the mean of the color and check its range within which range to know the plate type

2-Mohfza: each Governorate has its own plate so we check the number of letters and numbers and also check the first one or two letters to know the type of each one
