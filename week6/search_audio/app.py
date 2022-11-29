import argparse
from typing import List

import streamlit as st

from add_audio_data import (copy_audio_files, extract_audio_files,
                            filter_audio_data,
                            load_data_recersively_from_folders,
                            load_data_with_regex)
from elastic_search_utils import add_all_data, get_audio_file_path
from utils import State

# set the application title
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


def parse_args() -> argparse.Namespace:
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
    parser.add_argument("--regex", "-re", help="Add files with regular expression")
    return parser.parse_args()


if __name__ == "__main__":
    with st.spinner("Please wait while data is loading..."):
        args = parse_args()
        if State.audio_files_loaded == False:
            if args.audio_path_file:
                State.audio_files_loaded = extract_audio_files(args.audio_path_file)
            elif args.audio_path_dir:
                State.audio_files_loaded = copy_audio_files(args.audio_path_dir)
            elif args.recursive_files_extraction:
                State.audio_files_loaded = load_data_recersively_from_folders(
                    args.recursive_files_extraction
                )
            elif args.regex:
                State.audio_files_loaded = load_data_with_regex(args.regex)
            filter_audio_data()
        if State.files_added_to_elastcsearch == False:
            State.files_added_to_elastcsearch = add_all_data()
    display_main_page()
