import streamlit as st
from PIL import Image
import os

# Function to detect faces in the uploaded image
def detect_faces(image):
    # Dummy face detection function
    # Replace this with your actual face detection model
    # Here, I'm just checking if the image contains any face or not
    # You might need to use a more sophisticated face detection model
    # such as OpenCV's Haar Cascade Classifier or a deep learning-based model
    # to accurately detect faces
    return True if 'face' in image.lower() else False

# Function to display greeting message
def display_greeting():
    st.write("Welcome Ya habibi!")

# Function to play music
def play_music(audio_file):
    st.audio(audio_file, format='audio/mp3')

def main():
    st.title("Face Detection and Greeting Web App")
    st.write("Upload a photo to see if I can detect your face!")

    # Upload image
    uploaded_image = st.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'])

    if uploaded_image is not None:
        # Display uploaded image
        st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)
        
        # Check if image contains a face
        if detect_faces(uploaded_image.name):
            display_greeting()

        # Upload music
        uploaded_audio = st.file_uploader("Upload Music (MP3)", type=['mp3'])

        if uploaded_audio is not None:
            play_music(uploaded_audio)

if __name__ == '__main__':
    main()
