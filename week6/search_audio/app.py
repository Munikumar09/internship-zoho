import streamlit as st

from utils import get_audio_file_path

st.set_page_config("Audio Search")
audio_name: str = st.text_input("Please enter text to search: ")
if audio_name:
    audio_path: str = get_audio_file_path(audio_name)
    if not audio_path:
        st.write("No file found")
    else:
        with open(audio_path, "rb") as audio_file:
            # To display the audio file name
            st.write(f"audio file name: {(audio_path.split('/'))[-1]}")
            # To dispa
            st.audio(data=audio_file, format="audio/wav")
