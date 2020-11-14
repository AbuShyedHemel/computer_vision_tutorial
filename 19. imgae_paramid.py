import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('picture\lena.jpg')
# lr = cv2.pyrDown(img)
# lr1 = cv2.pyrDown(lr)
# lr2 = cv2.pyrUp(lr1)
layer = img.copy()
gp = [layer]

for i in range(5):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i),layer)

layer = gp[5]
cv2.imshow('upper level',layer)
lp = [layer]

for i in range(5,0,-1):
    gaussin = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussin)
    cv2.imshow(str(i),laplacian)


cv2.imshow('Original image',img)
# cv2.imshow('Pyr Down',lr)
# cv2.imshow('Pyr Down 1',lr1)
# cv2.imshow('Pyr UP 2',lr2)
cv2.waitKey(0)
cv2.destroyAllWindows()