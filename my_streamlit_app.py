import streamlit as st

def main():
    st.title("Set Background Image in Your Web App")
    
    # Upload image file
    uploaded_file = st.file_uploader("Upload Background Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        # Set background image using CSS with automatic adjustment
        st.markdown(
            f"""
            <style>
                .reportview-container {{
                    background: url(data:image/jpeg;base64,{uploaded_file.getvalue().hex()});
                    background-size: cover;
                    background-position: center;
                }}
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        # Default background image path
        default_background = "default.jpg"
        # Set default background image using CSS
        st.markdown(
            f"""
            <style>
                .reportview-container {{
                    background: url({default_background});
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
