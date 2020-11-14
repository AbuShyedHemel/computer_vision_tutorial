import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('picture\smarties.png',cv2.IMREAD_GRAYSCALE)
_,mask = cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)

kernal = np.ones((5,5),np.uint8)

dialation = cv2.dilate(mask,kernal,iterations=2)
erosion = cv2.erode(mask,kernal,iterations=1)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)
th = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)

title = ['image','mask','dialation','erosion','opening','closing','mg','th']
image = [img,mask,dialation,erosion,opening,closing,mg,th]

for x in range(8):
    plt.subplot(2,4,x+1),plt.imshow(image[x],'gray')
    plt.title(title[x])
    plt.xticks([]),plt.yticks([])
plt.show()