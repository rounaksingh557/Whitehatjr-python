# import the opencv library
import cv2

face_cascade = cv2.CascadeClassifier(
    "../DataSet/haarcascade_frontalface_default.xml")

eyes_cascade = cv2.CascadeClassifier("../DataSet/haarcascade_eye.xml")

# Define a video capture object
vid = cv2.VideoCapture(0)

while (True):

    # Capture the video frame by frame
    ret, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray)
    eyes = eyes_cascade.detectMultiScale(gray)

    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 3, 78), 3)

    # Display the resulting frame
    cv2.imshow("Web cam", frame)

    # Quit Window by Spacebar Key
    if cv2.waitKey(25) == 32:
        break

# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
