"""
Provide the functionalities that are required to extract and load audio files
"""
import os
import re
import shutil
import stat
import tarfile
from pathlib import Path, PurePath
from typing import Any, List, Match, Optional

import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from constants import AUDIO_FILE_DIR, TEMP_AUDIO_DIR
from elastic_search_utils import add_all_data


def reset_temp_directory() -> None:
    """
    Reset the temporary directory that means clear all the data from the temp directory
    """
    dst_path: Path = Path.cwd() / TEMP_AUDIO_DIR
    if os.path.exists(dst_path):
        shutil.rmtree(dst_path)
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)


def extract_audio_files(file_path: Path) -> bool:
    """
    Extract the audio files from provided file path and stores all the extracted
    audio files in local temp directory

    Args:
        file_path (Path): file path to extract audio files from

    Returns:
        bool: return True if successfully audio files were extracted
    """
    with tarfile.open(file_path) as tar_file:
        try:
            tar_file.extractall(f"./{TEMP_AUDIO_DIR}")
        except KeyError as key_error:
            print(key_error)
        finally:
            tar_file.close()
    return True


def add_individual_audio_file(src_path: Path) -> bool:
    """
    add a single audio file from given source path to temp directory

    Args:
        file_path (Path): source file path

    Returns:
        bool: return True if audio file is successfully added
    """
    dst_path: Path = Path.cwd() / TEMP_AUDIO_DIR
    shutil.copy(src=src_path, dst=dst_path)
    return True


def copy_audio_files() -> bool:
    """
    copy the audio files from temp directory to tmp/audio directory
    Args:
        file_path (str): audio files source path from where audio files will be copy

    Returns:
        bool: if copy operation success returns True else false
    """
    src_path: Path = Path.cwd() / TEMP_AUDIO_DIR
    dst_path: Path = Path(AUDIO_FILE_DIR)
    for file in src_path.iterdir():
        os.chmod(file, stat.S_IRWXU)
    res = shutil.copytree(src=src_path, dst=dst_path, dirs_exist_ok=True)
    return bool(res)


def tarfile_pattern_match(file_path: str) -> Optional[Match[Any]]:
    """
    This function checks the given file is tar file or not with regex
    Args:
        file (str): file name to validate the file is tar file or not

    Returns:
        Match[str] | None: if pattern matches return matched pattern else None
    """
    return re.search(r"[a-zA-Z0-9_ -]+\.tgz$", file_path)


def audio_pattern_match(file: str) -> Optional[Match[Any]]:
    """
    This function checks the given file is audio file or not with regex
    Args:
        file (str): file name to validate the file is audio file or not

    Returns:
        Match[str] | None: if pattern matches return matched patter else None
    """
    return re.search(r"[a-zA-Z0-9_-]+\.(opus|wav|mp3)$", file)


def add_audio_file_based_on_file_type(file_path: Path) -> bool:
    """
    Add the audio files based on the file extention means if it is tar file then
    extract all the files and place them into the temp folder. If it is audio file
    then directly add it into temp directory

    Args:
        file_path (Path): audio source file path

    Returns:
        bool: return True if the audio files were successfully added
    """
    if tarfile_pattern_match(str(file_path)):
        return extract_audio_files(file_path)
    if audio_pattern_match(str(file_path)):
        return add_individual_audio_file(file_path)
    return True


def fetch_audio_data_recursively(path: Path) -> bool:
    """
    This function recursively finds the tar fils and extract them into local audio directory
    Args:
        file_path_str (str): directory path to fetch all the audio files
    Returns:
        bool: return True if the audio files were successfully added
    """
    if path.is_file():
        add_audio_file_based_on_file_type(path)
    elif path.is_dir():
        for file in path.iterdir():
            fetch_audio_data_recursively(file)
    return True


def filter_audio_data() -> bool:
    """
    filter audio files from the local audio directory
    (some tar files contain other files along with audio files)
    Returns:
        bool: return True if the audio files were successfully filtered
    """
    audio_path: Path = Path.cwd() / TEMP_AUDIO_DIR
    for file in audio_path.iterdir():
        if not audio_pattern_match(str(file)):
            os.remove(file)
    return True


def load_data_from_folders(file_path: str) -> bool:
    """
    fetch audio files recursively from the given and filters the audio files

    file_path_str:
        file_path_str (str): source path to fetch audio files
    Returns:
        bool: return True if the audio files were successfully added
    """
    if os.path.exists(file_path):
        return fetch_audio_data_recursively(Path(file_path))
    return False


def match_file_regex_pattern(regex_str: str, file_path: str) -> Optional[Match[Any]]:
    """
    Validates given regex pattern against file path

    Args:
        regex_str (str): regular expression string
        file_path (str): file path to match with regex_str

    Returns:
        Match[str] | None: if pattern matches return matched patter else None
    """
    return re.search(regex_str, file_path)


def recursively_add_files_with_regex(regex_str: str, path: Path) -> bool:
    """
    add the files into the temp directory when the file matches the given regex pattern
    Args:
        regex_str (str): regular expression string
        path (Path): file path
    Returns:
        bool: return True when all the files were added
    """
    if path.is_file():
        if match_file_regex_pattern(regex_str, str(path)):
            return add_audio_file_based_on_file_type(path)
    elif path.is_dir():
        for file in path.iterdir():
            recursively_add_files_with_regex(regex_str, file)
    return True


def regex_to_path(regex_str: str) -> str:
    """
    constructs the initial path (from here searching and regex validation starts)
    from the given regex

    Args:
        regex_str (str): regular expression string

    Returns:
        str: inital Path to start search
    """
    path_split_list: List[str] = regex_str.split("/")
    path: PurePath = PurePath("/")
    for i in range(len(path_split_list) - 1):
        path_split_list[i] = path_split_list[i].strip("()*_- ")
        path = path.joinpath(path_split_list[i])
    if str(path) == "/":
        return ""
    return str(path)


def load_data_with_regex(regex_str: str) -> bool:
    """
    Load the audio files with regex pattern matching

    Args:
        regex_str (str): regular expression string

    Returns:
        bool: Return True if successfully loads the data else False
    """
    initial_path: str = regex_to_path(regex_str)
    if os.path.exists(initial_path):
        recursively_add_files_with_regex(regex_str, Path(initial_path))
        return True
    return False


def add_audio_files(audio_path_input: str) -> bool:
    """
    This function will add the audio files based on the input path

    Args:
        audio_path_input (str): input file or folder path

    Returns:
        bool: return True if audio files were successfully added
    """
    if audio_path_input:
        status: DeltaGenerator = st.text("fetching data from source files...")
        reset_temp_directory()
        audio_path: List[str] = audio_path_input.split(" ")
        data_loaded: bool = False
        if len(audio_path) > 1:
            data_loaded = load_data_with_regex(audio_path[0])
        else:
            data_loaded = load_data_from_folders(audio_path[0])
        if data_loaded:
            status.text("Adding documents to the elasticsearch...")
            is_copied_and_added_to_index = (
                copy_audio_files() and filter_audio_data() and add_all_data()
            )
            status.text("")
        return is_copied_and_added_to_index
    return False
