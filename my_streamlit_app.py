import streamlit as st
import cv2
import os
from playsound import playsound

def detect_and_capture_face():
    # Load pre-trained face detection model
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Display the frame
        st.image(frame, channels="BGR")
        
        # Capture an image if a face is detected
        if len(faces) > 0:
            cv2.imwrite('customer_image.jpg', frame)  # Save the captured image
            break
        
        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

def play_crowd_noise():
    # Play crowd noise effect
    crowd_noise_file = 'crowd_noise.mp3'  # Place your crowd noise audio file in the same directory
    playsound(crowd_noise_file)

def main():
    st.title("Welcome System for Customers")

    # Button to trigger face detection and capture
    if st.button("Detect and Capture Face"):
        detect_and_capture_face()
        play_crowd_noise()
        st.success("Welcome! Your face has been captured.")

if __name__ == '__main__':
    main()
