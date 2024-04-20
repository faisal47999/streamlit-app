import streamlit as st
import cv2
from PIL import Image
import numpy as np

# Function to detect faces using OpenCV
def detect_faces(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Load the pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

# Function to overlay celebrity welcome message on detected face
def overlay_celebrity_welcome(image, face):
    # Load the celebrity welcome message image
    celebrity_img = cv2.imread('celebrity_welcome.png')
    # Resize the celebrity welcome message to fit the detected face
    celebrity_img = cv2.resize(celebrity_img, (face[2], face[3]))
    # Overlay the celebrity welcome message on the detected face
    x_offset, y_offset = face[0], face[1]
    image[y_offset:y_offset+celebrity_img.shape[0], x_offset:x_offset+celebrity_img.shape[1]] = celebrity_img
    return image

# Main function to run the Streamlit web app
def main():
    st.title("Celebrity Welcome Web App with Face Detection")

    # Webcam capture using OpenCV
    cap = cv2.VideoCapture(0)

    # Main app loop
    while True:
        # Read frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Detect faces in the frame
        faces = detect_faces(frame)

        # Overlay celebrity welcome message on each detected face
        for face in faces:
            frame = overlay_celebrity_welcome(frame, face)

        # Convert the frame to RGB format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame with Streamlit
        st.image(frame_rgb, channels="RGB")

        # Check if the user clicked the 'Stop' button
        if st.button("Stop"):
            break

    # Release the webcam and close the Streamlit app
    cap.release()

if __name__ == "__main__":
    main()
