import cv2

img = cv2.imread("Image/poster.jpg")
rocket = img[120:360, 400:500]
img[0:240, 500:600] = rocket
text = "This is an edited image using opencv and python"
cv2.putText(img, text, (9, 100),
            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(0, 0, 255))
cv2.imshow("Output", img)
cv2.waitKey(0)
