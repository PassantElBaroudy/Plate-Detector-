# Plate-Detector-

VIDEO LINK: https://youtu.be/DwdHsuaTzb4



# Team Members:
1-Andrew Rafaat

2-Pavly Mario

3-Passant Mohamed 

4-Salah Adel

5-Youssef Rafaat

 # Requirements:
 

# Description:
•The project idea is to implement an image processing algorithm that aims to detect the vehicle plate’s type and its governorate in a given image and detect the characters and numbers in it , It also detects the car’s owner information ( Name and Age ) and it detects the car’s model and traffic violations .



# Implementation:
GENERAL IDEA: The idea of the project: is to take the image to plate enhancement function which does all the pre-processing then split plate takes it to divide the image into two parts letters and characters
to give it to nums and chars function to get the number of chars and numbers to give it to mohfza function to know the name of Governorate
then function split splits the chars and numbers images into each number and each letter alone in a picture so function OCR takes it to get the numbers and letters
in parallel to that function plate types is working to know the color of the plate to know the type of the plate 
then connects the letters and numbers with the database to get the info we needed for this car we access all of this through GUI
you can check source file to know the type of each plate and it's Governorate


1-PlateType: This function takes the plate image then resize it and crop the image to get the upper part and apply some functions to get the pixels of the image and its values then 
get the mean of the color and check its range within which range to know the plate type

2-Mohfza: each Governorate has its own plate so we check the number of letters and numbers and also check the first one or two letters to know the type of each one










# User Guide:
![Test Case](https://github.com/PassantElBaroudy/Plate-Detector-/blob/main/source/vpd.PNG)


1- Browse to choose the image 

2- press submit , the info will appear

3- you can exit if you don't want to browse another plate or you can press refresh to browse another plate


