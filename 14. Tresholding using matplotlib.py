import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('picture\gradient.png',0)
_, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img,200,255,cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

title = ['ORIGINAL','BINARY','BINARY_INV','TRUNC','TOZEROS','TOZEROS_INV']
images = [img,th1,th2,th3,th4,th5]

for x in range(6):
    plt.subplot(2,3,x+1),plt.imshow(images[x],'gray')
    plt.title(title[x])
    plt.xticks([]),plt.yticks([])
plt.show()