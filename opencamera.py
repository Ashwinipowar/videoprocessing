import cv2
cap=cv2.VideoCapture(0)
#this 0 we use for the webcam

while True:
    ret ,frame =cap.read()


    if not ret:
        print("could not read frame")
        break
    cv2.imshow("webcam feed",frame)

    if cv2.waitKey(1)& 0xFF ==ord('q'):
        print("quitting....")
        break
cap.release()

cv2.destroyAllWindows()
