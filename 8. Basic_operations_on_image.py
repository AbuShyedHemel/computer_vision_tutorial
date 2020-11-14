import cv2
import numpy as np

img = cv2.imread('picture\messi5.jpg')
img2 = cv2.imread('picture\opencv-logo.png')

print(img.size)
print(img.shape)
print(img.dtype)


b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

dst = cv2.add(img,img2)

#cv2.imshow('add',dst)
dst = cv2.addWeighted(img,.5,img2,.5,0)
# img = cv2.imread('picture\messi5.jpg')
cv2.imshow('image',dst)
# cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()