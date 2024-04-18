import streamlit as st
import os
from playsound import playsound

def detect_and_capture_face(uploaded_file):
    if uploaded_file is not None:
        # Save the uploaded photo
        with open("customer_image.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Play crowd noise effect
        play_crowd_noise()
        
        # Display success message
        st.success("Welcome! Your face has been captured.")

def play_crowd_noise():
    # Play crowd noise effect
    crowd_noise_file = 'crowd_noise.mp3'  # Place your crowd noise audio file in the same directory
    playsound(crowd_noise_file)

def main():
    st.title("Welcome System for Customers")

    # File uploader to upload a photo
    uploaded_file = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])

    # Button to trigger face detection and capture
    if st.button("Detect and Capture Face"):
        detect_and_capture_face(uploaded_file)

if __name__ == '__main__':
    main()
