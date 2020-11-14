import cv2

cap    = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out    = cv2.VideoWriter('video\\vid001.avi',fourcc,20.0,(640,480))

while (cap.isOpened()): 
    ret, frame = cap.read()

    if ret == True:
        width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(width,height)

        out.write(frame)

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('video',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: 
        break
cap.release()
out.release()
cv2.destroyAllWindows()