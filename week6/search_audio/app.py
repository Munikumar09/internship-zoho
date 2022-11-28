import argparse
from typing import List

import streamlit as st

from add_audio_data import copy_audio_files, extract_audio_files, load_data
from elastic_search_utils import add_all_data, get_audio_file_path

ss = st.session_state
if "audio" not in ss:
    ss["audio"] = False
if "files" not in ss:
    ss["files"] = False
st.set_page_config("Audio Search")


def display_main_page():
    audio_name: str = st.text_input("Please enter audio file name to search: ")
    if audio_name:
        audio_path_list: List[str] = get_audio_file_path(audio_name)
        if len(audio_path_list) == 0:
            st.write("No file found")
        else:
            for audio_path in audio_path_list:
                with open(audio_path, "rb") as audio_file:
                    # To display the audio file name
                    st.write(f"audio file name: {(audio_path.split('/'))[-1]}")
                    # To dispalay the audio file
                    st.audio(data=audio_file, format="audio/wav")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--recursive-files-extraction",
        "-r",
        help="File path to recersively search and extract audio files",
    )
    parser.add_argument(
        "--audio-path-file", "-f", help="Path to the audio file (tar format)"
    )
    parser.add_argument(
        "--audio-path-dir",
        "-d",
        help="Path to the directory that contain the audio files",
    )
    return parser.parse_args()


if __name__ == "__main__":
    with st.spinner("Please wait while data is loading..."):
        args = parse_args()
        if ss["audio"] == False:
            if args.audio_path_file:
                ss["audio"] = extract_audio_files(args.audio_path_file)
            elif args.audio_path_dir:
                ss["audio"] = copy_audio_files(args.audio_path_dir)
            elif args.recursive_files_extraction:
                ss["audio"] = load_data(args.recursive_files_extraction)
        if ss["files"] == False:
            ss["files"] = add_all_data()
    display_main_page()
