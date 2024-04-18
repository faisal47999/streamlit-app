import streamlit as st
from PIL import Image
from playsound import playsound

def apply_photo_frame(image):
    # Load the photo frame image
    photo_frame = Image.open("photo_frame.png")

    # Resize the photo frame to match the image dimensions
    resized_frame = photo_frame.resize(image.size)

    # Apply the photo frame overlay
    framed_image = Image.alpha_composite(image.convert("RGBA"), resized_frame)

    return framed_image

def play_welcome_sound():
    # Play welcoming message and crowd noise effect
    CROWD_NOISE_FILE = 'crowd_noise.mp3'  # Path to the crowd noise audio file
    playsound(CROWD_NOISE_FILE)

def main():
    st.title("Welcome System for Customers")

    # File uploader to upload a photo
    uploaded_file = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the uploaded image
        image = Image.open(uploaded_file)

        # Apply the photo frame overlay
        framed_image = apply_photo_frame(image)

        # Display the image with the photo frame overlay
        st.image(framed_image, caption='Welcome!', use_column_width=True)

        # Play welcoming sound
        play_welcome_sound()

if __name__ == '__main__':
    main()
