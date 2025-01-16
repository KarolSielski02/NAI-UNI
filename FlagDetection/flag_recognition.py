import cv2
import numpy as np
from tensorflow.keras.models import load_model

"""
Flag Recognition Script

Authors: Tomasz Wasielewski, Karol Sielski

This script captures video from the camera, detects a flag in the frame, and classifies it as Polish, Russian, or 
Ukrainian using a pre-trained deep learning model. The detected flag region is highlighted with a bounding box, and the 
predicted label is displayed on the frame.

Steps:
1. Load the pre-trained flag recognition model.
2. Define the labels for the classification.
3. Define a function to preprocess the frame for prediction.
4. Define a dummy function to get the bounding box of the flag (for demonstration purposes).
5. Capture video from the camera.
6. For each frame:
   a. Get the bounding box of the flag.
   b. Crop the flag region from the frame.
   c. Preprocess the flag region.
   d. Predict the flag using the pre-trained model.
   e. Draw a bounding box around the detected flag.
   f. Display the predicted label on the frame.
   g. Show the frame.
   h. Break the loop on 'q' key press.
7. Release the video capture and close the window.
"""

# Load the pre-trained model
model = load_model('flag_recognition_model.keras')

# Define the labels
labels = ['Polish', 'Russian', 'Ukrainian']


# Function to preprocess the frame
def preprocess_frame(frame):
    frame = cv2.resize(frame, (224, 224))
    frame = frame / 255.0
    frame = np.expand_dims(frame, axis=0)
    return frame


# Dummy function to get the bounding box of the flag
def get_flag_bounding_box(frame):
    height, width, _ = frame.shape
    x, y, w, h = width // 4, height // 4, width // 2, height // 2
    return x, y, w, h


# Capture video from the camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Get the bounding box of the flag
    x, y, w, h = get_flag_bounding_box(frame)

    # Crop the flag region from the frame
    flag_region = frame[y:y + h, x:x + w]

    # Preprocess the flag region
    preprocessed_frame = preprocess_frame(flag_region)

    # Predict the flag
    predictions = model.predict(preprocessed_frame)
    label = labels[np.argmax(predictions)]

    # Draw a bounding box around the detected flag
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the label on the frame
    cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Show the frame
    cv2.imshow('Flag Recognition', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
