import cv2
import datetime

cap = cv2.VideoCapture(0)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(width,height)

# cap.set(3,1208)
# cap.set(4,1208)
#
# print(cap.get(3))
# print(cap.get(4))

while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:

        date = str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_DUPLEX
        text = 'Width: '+str(cap.get(3))+'Height: '+str(cap.get(4))
        frame = cv2.putText(frame,text,(10,50),font,1,(255,255,0),3,cv2.LINE_AA)
        frame = cv2.putText(frame, date, (20, 200), font, 1, (0, 255, 0), 3, cv2.LINE_AA)

        img = cv2.rectangle(frame,(384,0),(510,128),(0,0,255),6)
        cv2.imshow('video',img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()