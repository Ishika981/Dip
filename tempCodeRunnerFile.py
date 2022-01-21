import cv2
imag1 = cv2.imread('i1.jpg', 1)
imag2 = cv2.imread('imag.jpg', 1)

imag1 = cv2.resize(imag1,(512,512))
imag2 = cv2.resize(imag2,(512,512))

img = cv2.add(imag1, imag2)

cv2.imshow('image', img)
added = 'add.jpg'

cv2.imwrite(added, img)

cv2.waitKey(0)