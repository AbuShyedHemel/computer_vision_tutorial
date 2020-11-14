import cv2
import numpy as n

img  = cv2.imread('picture\pic1.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners  = cv2.goodFeaturesToTrack(gray, 100, 0.01,  30)

corners = n.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y),  3, 255, -1)

cv2.imshow('dst', img)

if  cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()