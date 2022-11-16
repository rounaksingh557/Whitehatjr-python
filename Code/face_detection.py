import cv2

img = cv2.imread("../Image/Face Detection/boy.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(
    '../DataSet/haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray)
print(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Crop the image and save the image in a separate file
    face_specific = img[y:y+h, x:x+w]
    cv2.imwrite("boyface.jpg", face_specific)

cv2.imshow('img', img)
cv2.waitKey(0)
