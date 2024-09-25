import tensorflow as tf
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os

# test

# Load the saved TensorFlow model when the module is imported
model = load_model(os.path.join('models', 'attentionmodel.h5'))


def classify_image(image_path):
    """
    Function to classify whether a person in the image is sleeping or paying attention.

    Parameters:
    - image_path: str, path to the image to be classified

    Returns:
    - str, classification result ("Student is sleeping :(" or "Student is paying attention :)")
    """
    # Load the image using OpenCV
    img = cv2.imread(image_path)

    if img is None:
        return "Image not found!"

    # Convert the image from BGR (OpenCV default) to RGB
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize the image to the size the model expects (256x256)
    resized_img = tf.image.resize(rgb_img, (256, 256))

    # Normalize the image (scale pixel values between 0 and 1)
    resized_img = resized_img / 255.0

    # Expand dimensions to match the model's input shape (batch_size, height, width, channels)
    input_image = np.expand_dims(resized_img, axis=0)

    # Make a prediction using the loaded model
    yhat = model.predict(input_image)

    # Interpret the prediction result
    if yhat > 0.5:
        return 'Student is sleeping :('
    else:
        return 'Student is paying attention :)'
