import cv2

face_cascade = cv2.CascadeClassifier('HarcascadeClassifire\eface_cascade.xml')
cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, frame = cap.read()

    gary = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gary, 1.1, 4)

    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x + w, y+h), (255, 0, 0), 3)

    cv2.imshow('img', frame)
    if  cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
