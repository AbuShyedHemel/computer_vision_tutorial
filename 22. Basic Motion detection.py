import cv2
import numpy as np

cap = cv2.VideoCapture('picture\hvtest.avi')
ret, frame = cap.read()
ret, frame1 = cap.read()

while(cap.isOpened()):
    diff = cv2.absdiff(frame,frame1)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur,20,255, cv2.THRESH_BINARY)
    dialated = cv2.dilate(thresh, None, iterations=3)
    contures, _ = cv2.findContours(dialated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #cv2.drawContours(frame, conture, -1, (0, 255, 0), 3)
    for conture in contures:
        (x, y, w, h) = cv2.boundingRect(conture)

        if cv2.contourArea(conture) < 900 :
            continue
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Status: {}".format('Movement'), (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)


    cv2.imshow('feed',frame)
    frame = frame1
    ret, frame1 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()