# import the opencv library
import cv2
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("../DataSet/keras_model.h5")


# define a video capture object
vid = cv2.VideoCapture(0)

while (True):

    # Capture the video frame by frame
    ret, frame = vid.read()

    image = cv2.resize(frame, (224, 224))
    test_image = np.array(image, dtype=np.float32)
    test_image = np.expand_dims(test_image, 0)
    normalized_image = test_image/255.0
    prediction = model.predict(normalized_image)
    print(prediction)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Quit window with spacebar
    key = cv2.waitKey(1)

    if key == 32:
        break

# After the loop release the cap object
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
