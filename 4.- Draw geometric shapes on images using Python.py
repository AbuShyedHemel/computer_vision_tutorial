import cv2

img = cv2.imread('picture\ml.png',0)

img = cv2.line(img,(0,0),(255,255),(255,0,0),2) 
img = cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),2)
img = cv2.rectangle(img,(330,390),(280,340),(0,0,255),6)
img = cv2.circle(img,(100,100),63,(0,0,255),6)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,'OpenCV',(10,500),font,4,(255,0,0),6)
cv2.imshow('lena',img)


cv2.waitKey(0)
cv2.destroyAllWindows()