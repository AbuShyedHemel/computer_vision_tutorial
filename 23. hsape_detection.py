import cv2
import numpy as np

img = cv2.imread('picture\shapes.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(imgray,240, 255, cv2.THRESH_BINARY)
contoures , _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contoures:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength (contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 255, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectRation = float(w)/h
        print(aspectRation)
        if aspectRation >= 0.95 and aspectRation <= 1.05:
            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
        else:
            cv2.putText(img,"Retangle", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0,0))
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
    elif len(approx) == 10:
        cv2.putText(img, "Start", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
    else:
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()