import cv2
import numpy as np

cap = cv2.VideoCapture('picture\slow_traffic.mp4')
ret , frame = cap.read()

x, y, width, height  = 300, 200, 100, 50
track_window = (x, y, width, height)

roi = frame[y:y+height, x:x+width]
hsv_roi =  cv2.cvtColor(roi,  cv2.COLOR_BGR2HSV)
mask  = cv2.inRange(hsv_roi,np.array((0.,60., 32.)), np.array((180., 255., 255)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

term_crit = (cv2.TERM_CRITERIA_EPS  | cv2.TERM_CRITERIA_COUNT,  10,  1)
cv2.imshow('roi', roi)
while(1):
    ret, frame = cap.read()
    if ret == True:

        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],  [0],  roi_hist, [0, 180], 1)
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)
        pts = cv2.boxPoints(ret)
        print(pts)
        pts = np.int0(pts)
        final_iamge = cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

        x,y ,w,h  =  track_window
        final_iamge = cv2.rectangle(frame, (x,y), (x+w, y+h), 255, 3)

        cv2.imshow('dst', dst)
        cv2.imshow('frame', frame)
        k = cv2.waitKey(30) & 0xFF
        if k == 27:
            break
    else:
        break