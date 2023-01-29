import cv2
import tensorflow as tf
import mss
import numpy as np
import time

# Load the model
model = tf.keras.models.load_model('.\converted_keras\keras_model.h5')

# Create a mss object
sct = mss.mss()

while True:
    # Take a screenshot of the screen
    sct_img = sct.grab(sct.monitors[1])

    # Convert the image to a numpy array
    img = np.array(sct_img)

    #Convert BGRA to BGR
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    # Resize the screenshot to the input size of the model
    img = cv2.resize(img, (224, 224))

    # Convert the image to a 4D tensor
    img = img[tf.newaxis, ...]

    # Use the model to make a prediction
    prediction = model.predict(img)
    
    print(prediction)
    # Check if the content is present on the screen
    if prediction[0][0] > prediction[0][1]:
        print("Chrome is open.")
    elif prediction[0][1] > prediction[0][0]:
        print("Chrome is open but not selected.")
    else:
        print("Chrome is not open.")

    # Wait for some time before taking the next screenshot
    time.sleep(1)