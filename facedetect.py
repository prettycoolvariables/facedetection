import cv2
camera=cv2.VideoCapture(0)
facedetector=cv2.CascadeClassifier("face.xml")
while True:
    success,frame=camera.read()
    if success:
        img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        face=facedetector.detectMultiScale(img,minNeighbors=10)
        print(face)
        for x,y,w,h in face:
            print(x,y,w,h)
            if x<480 and y<640:
                frame[x,y]=(0,255,0)
                frame[x,y+1]=(0,255,0)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("output",frame)
        k=cv2.waitKey(1)
        if k==ord(" "):       
            camera.release()
            cv2.destroyAllWindows()
            break                            
