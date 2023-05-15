
import cv2
import numpy as np
import tensorflow as tf

# Load the PoseNet model
model = tf.keras.models.load_model('model-stride8.json')

# Define the exercises to detect
exercises = {
    'squat': [11, 12, 23, 24],
    'pushup': [5, 6, 7, 8, 11, 12],
    'lunge': [11, 12, 13, 14, 23, 24, 25, 26],
}

# Define a function to analyze a pose and detect exercises
def detect_exercises(pose):
    for exercise, keypoints in exercises.items():
        if all(pose[keypoint][2] > 0 for keypoint in keypoints):
            print(f'Detected {exercise}!')
            # Do something here, like incrementing a counter or sending a notification

# Start capturing video
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale and resize it
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    small_gray = cv2.resize(gray, (256, 256))

    # Normalize the pixel values to be between 0 and 1
    small_gray_norm = small_gray / 255.0

    # Add a batch dimension to the frame
    input_image = np.expand_dims(small_gray_norm, axis=0)

    # Run the PoseNet model to estimate poses
    outputs = model(input_image)
    poses = outputs[-1].numpy()

    # Analyze each pose and detect exercises
    for pose in poses:
        detect_exercises(pose)

    # Show the frame
    cv2.imshow('frame', frame)
