import cv2
camera = cv2.VideoCapture(0)

while True:
    ret,frame = camera.read()

    if not ret:
        print("camera open nahi hua h")
        break
    cv2.imshow("camera test",frame)


    if cv2.waitKey(1) & 0xff ==ord("q"):
        break
camera.release()
cv2.destroyAllWindows()

