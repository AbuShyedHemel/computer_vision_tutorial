import cv2
import numpy as np

cap = cv2.VideoCapture('picture\mvtest.avi')
#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG() #background object of  the function
#fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG(detectShadows=True)
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=False)


while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('Frame', frame)
    cv2.imshow('Frame1', fgmask)

    keyboard  = cv2.waitKey(30)
    if keyboard  == 'q' or keyboard == 27:
        break
cap.release()
cv2.destroyAllWindows()