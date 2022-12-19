import cv2
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("../DataSet/keras_model_for_rock.h5")

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()

    frame = cv2.flip(frame, 1)

    image = cv2.resize(frame, (224, 224))
    test_image = np.array(image, dtype=np.float32)
    test_image = np.expand_dims(test_image, 0)
    normalized_image = test_image/255.0
    prediction = model.predict(normalized_image)

    rock = int(prediction[0][0]*100)
    paper = int(prediction[0][1]*100)
    scissor = int(prediction[0][2]*100)

    print(f"Rock: {rock} %, Paper: {paper} %, Scissor: {scissor} %")

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)

    if key == 32:
        break

vid.release()

cv2.destroyAllWindows()
