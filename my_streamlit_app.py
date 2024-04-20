import streamlit as st

def main():
    # Background image path
    background_path = "D:/background.jpg"

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
    st.title("How to Set a Background Image in Your Web App")
    
    st.write("""
    **Introduction:** 
    In today's digital age, creating visually appealing web applications is essential to engage users and provide them with a seamless experience. One effective way to enhance the aesthetics of your web app is by setting a background image. A captivating background can instantly grab users' attention and make your app stand out. In this tutorial, we'll explore how you can easily set a background image in your web app using Streamlit, a popular Python library for building interactive web applications.
    
    **Outline:**
    1. **Introduction to Background Images**
       - Why background images are important
       - Examples of effective background images in web apps
    2. **Setting Up Your Streamlit Environment**
       - Installing Streamlit
       - Creating a new Streamlit app file
    3. **Adding a Background Image**
       - Choosing the right image
       - Understanding file paths
       - Using CSS to set the background image
    4. **Testing Your Web App**
       - Running the Streamlit app locally
       - Troubleshooting common issues
    5. **Deploying Your Web App**
       - Hosting options for Streamlit apps
       - Deploying your app on GitHub Pages or Streamlit Sharing
    6. **Conclusion**
       - Recap of key points
       - Encouragement to experiment and personalize your web app's background
    
    **Key Takeaways:**
    - Background images can enhance the visual appeal of your web app and create a memorable user experience.
    - Streamlit provides a simple yet powerful platform for building interactive web applications in Python.
    - By following a few steps, you can easily set a background image in your Streamlit web app and deploy it for the world to see.
    
    **Call to Action:**
    Ready to transform your web app with a stunning background image? Follow along with our tutorial and take your web development skills to the next level!
    """)

if __name__ == "__main__":
    main()
