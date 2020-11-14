import cv2
from matplotlib import pyplot as plt
import numpy as np

#img = cv2.imread('picture\opencv-logo.png')#for dst,blur
#img = cv2.imread('picture\water.png')#for median
img = cv2.imread('picture\lena.jpg')#for bilateralfilter
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

kernal = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernal)
blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)
bilateralfilter = cv2.bilateralFilter(img,9,75,75)

title = ['image','2D Convolution','blur','gblur','median','bilateralfilter']
image = [img,dst,blur,gblur,median,bilateralfilter]

for x in range(6):
    plt.subplot(2,3,x+1),plt.imshow(image[x],'gray')
    plt.title(title[x])
plt.show()