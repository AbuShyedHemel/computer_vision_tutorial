import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('HarcascadeClassifire\eface_cascade.xml')
eye_cascad = cv2.CascadeClassifier("HarcascadeClassifire\haarcascade_eye.xml")
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in face:
        roi_gary = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascad.detectMultiScale(roi_gary)
        for (ex, ey, ew, eh) in eyes:
            new = cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()