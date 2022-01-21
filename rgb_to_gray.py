import numpy as np
import cv2 

img = cv2.imread('i1.jpg')
cv2.imshow('image',img)

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', grayscale)
filename = 'i2.jpg'

cv2.imwrite(filename, grayscale)
  