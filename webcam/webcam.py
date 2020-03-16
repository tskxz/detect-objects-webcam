import cv2

webcam = cv2.VideoCapture(0)

while True:
    check, frame = webcam.read()
    print(check)
    print(frame)
    cv2.imshow("WEBCAM", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
