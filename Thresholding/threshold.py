import cv2

webcam = cv2.VideoCapture(0)
first_frame = None

while True:
    check, frame = webcam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    thresh_frame_a = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY_INV)[1]
    thresh_frame_a = cv2.dilate(thresh_frame_a, None, iterations=2)

    # Show images
    cv2.imshow("DELTA", delta_frame)
    cv2.imshow("Thresh BINARY/30", thresh_frame)
    cv2.imshow("THRESH BINARY_INV", thresh_frame_a)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
