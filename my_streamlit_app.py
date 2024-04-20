import streamlit as st

def main():
    # Background image path
    background_path = "D:/background.jpg!bw700"  # Update this with your image path

    # Set background image using HTML
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
    st.title("Welcome to My Web App")
    st.write("This is the content of my web app.")

if __name__ == "__main__":
    main()
