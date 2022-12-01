"""
Display the main page of streamlit application.
"""
import os
from typing import List

import streamlit as st

from add_audio_data import add_audio_files
from elastic_search_utils import create_index, get_audio_file_path

# set the application title
st.set_page_config("Audio Search")


def display_main_page():
    """
    Display the main page with text_input widget to get the audio flile name as input
    """
    form = st.sidebar.form("audio path input form", clear_on_submit=True)
    audio_path = form.text_input("Please enter the path to load the audio file")
    is_button_clicked = form.form_submit_button("load audio file")
    if audio_path and is_button_clicked:
        with st.spinner("Please wait while data is loading..."):
            add_audio_files(audio_path)
    audio_name: str = st.text_input("Please enter audio file name to search: ")
    if audio_name:
        audio_path_list: List[str] = get_audio_file_path(audio_name)
        if len(audio_path_list) == 0:
            st.write("No file found")
        else:
            for audio_path in audio_path_list:
                if os.path.exists(audio_path):
                    with open(audio_path, "rb") as audio_file:
                        # To display the audio file name
                        st.write(f"audio file name: {(audio_path.split('/'))[-1]}")
                        # To dispalay the audio file
                        st.audio(data=audio_file, format="audio/wav")


if __name__ == "__main__":
    create_index()
    display_main_page()
