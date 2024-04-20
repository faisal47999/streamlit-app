import streamlit as st

def main():
    st.title("Set Background Image in Your Web App")
    
    # Upload image file
    uploaded_file = st.file_uploader("Upload Background Image", type=["jpg", "jpeg", "png"])

    # Background image path
    background_path = "background.jpg"

    if uploaded_file is not None:
        # Save the uploaded file locally
        with open("background.jpg", "wb") as f:
            f.write(uploaded_file.getvalue())
        # Update background image path
        background_path = "background.jpg"

    # Set background image using CSS
    st.markdown(
        f"""
        <style>
            .reportview-container {{
                background: url('{background_path}');
                background-size: cover;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Your Streamlit app content
    st.write("This is the content of your web app.")

if __name__ == "__main__":
    main()
