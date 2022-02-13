import numpy as np
import matplotlib.pyplot as plt
import cv2 

img = cv2.imread('i1.jpg')


R,C,channel = img.shape
gray_img = np.zeros((R,C))

for i in range(R) :
    for j in range(C):
        x = int(img[i,j,0])+ int(img[i,j,1])+ int(img[i,j,2])
        x = x/3
        gray_img[i][j] = x


filename = 'GREY_i1.jpg'
  
# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, gray_img)
  