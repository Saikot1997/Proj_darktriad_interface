import streamlit as st
from pathlib import Path


def front_page():
    # st.header("Page Front Content")
    # Graphic
    # title
    # intro
    show_initial_text()

def show_initial_text():
    st.subheader("Questionnaire Overview")
    st.markdown("""
        This **interactive web interface** offers a quick and engaging way to assess your :red[psychopatic, narcistic, and Machiavellian tendencies]. 
        No lengthy explanations or excessive reading required!
        
        """)

    st.markdown("Simply answer 28 questions by selecting a score from :red[1  (strongly disagree)] to :violet[5 (strongly agree)]. It's as easy as giving your honest opinion.")
    st.markdown(" ")
    st.markdown(" ")
    import os
    # Display an image from a file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_file = os.path.join(current_dir, "chess (1).jpg")

    st.image(image_file, use_column_width=True)
