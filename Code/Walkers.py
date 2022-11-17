import cv2

# Create our body classifier
body_cascade = cv2.CascadeClassifier("../DataSet/haarcascade_fullbody.xml")

# Initiate video capture for video file
cap = cv2.VideoCapture('../Video/walking.avi')

# Loop once video is successfully loaded
while True:

    # Read first frame
    ret, frame = cap.read()

    # Convert Each Frame into Grayscale
    grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Pass frame to our body classifier
    body = body_cascade.detectMultiScale(grayScale, 1.2, 3)

    # Extract bounding boxes for any bodies identified
    for (x, y, w, h) in body:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 245, 255), 3)

    cv2.imshow("Video of pedestrian", frame)

    if cv2.waitKey(1) == 32:  # 32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
