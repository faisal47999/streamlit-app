import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from playsound import playsound

# Load crowd noise audio file
CROWD_NOISE_FILE = 'crowd_noise.mp3'

def detect_faces(image):
    # Load pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    return faces

def apply_effects(image, faces):
    # Load photo frame image
    frame_img = cv2.imread('photo_frame.png', cv2.IMREAD_UNCHANGED)

    # Apply photo frame around detected faces
    for (x, y, w, h) in faces:
        resized_frame = cv2.resize(frame_img, (w, h))  # Resize the frame to match face size
        image[y:y+h, x:x+w] = np.where(resized_frame[...,3]==255, resized_frame[:,:,:3], image[y:y+h, x:x+w])

    return image

def play_welcome_sound():
    # Play welcoming message and crowd noise effect
    playsound(CROWD_NOISE_FILE)

def main():
    st.title("Welcome System for Customers")

    # File uploader to upload customer's photo
    uploaded_file = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read uploaded image
        image = Image.open(uploaded_file)
        img_array = np.array(image)

        if img_array.size > 0:  # Check if the image is not empty
            # Detect faces in the image
            faces = detect_faces(img_array)

            if len(faces) > 0:  # Check if faces are detected
                # Apply photo frame around detected faces
                image_with_effects = apply_effects(img_array, faces)

                # Display image with effects
                st.image(image_with_effects, caption='Welcome!', use_column_width=True)

                # Play welcoming sound
                play_welcome_sound()
            else:
                st.error("No faces detected in the uploaded photo.")
        else:
            st.error("Uploaded photo is empty or invalid.")

if __name__ == '__main__':
    main()
