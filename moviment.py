# Import open-cv2 python module
import cv2

# Webcam
video = cv2.VideoCapture(0)
first_frame = None

# Infinite looop
while True:
    # Loads the webcam camera
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY_INV)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (_, cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Delta
    cv2.imshow("DELTA FRAME", delta_frame)

    # Thresh
    cv2.imshow("THRESH FRAME", thresh_frame)

    # Detect objects
    cv2.imshow("Image", frame)

    print(gray)
    print(delta_frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
