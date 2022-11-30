"""
Provide the functionalities that are required to extract and load audio files
"""
import os
import re
import shutil
import tarfile
from pathlib import Path, PurePath
from typing import Any, List, Match, Optional

from utils import AUDIO_FILE_DIR, State


def delete_existing_audio_dir() -> None:
    """
    Delete local audio directory if it exists in the current working directory
    """
    curr_path: Path = Path.cwd()
    for file in curr_path.iterdir():
        if file.name == AUDIO_FILE_DIR:
            shutil.rmtree(file)


def extract_audio_files(file_path: Path, delete_existing_dir: bool = True) -> bool:
    """
    Extract the audio files from provided file path and stores all the extracted
    audio files in local audio directory

    Args:
        file_path (Path): file path to extract audio files from
        delete_existing_dir (bool, optional): deletes the local audio directory if exits.
        Defaults to True.

    Returns:
        bool: return True if successfully audio files were extracted
    """
    if delete_existing_dir:
        delete_existing_audio_dir()
    with tarfile.open(file_path) as tar_file:
        try:
            tar_file.extractall(f"./{AUDIO_FILE_DIR}")
        except KeyError as key_error:
            print(key_error)
        finally:
            tar_file.close()
    return True


def copy_audio_files(file_path: str) -> bool:
    """
    copy the audio files from source directory to local audio directory for easy access
    Args:
        file_path (str): audio files source path from where audio files will be copy

    Returns:
        bool: if copy operation success returns True else false
    """
    delete_existing_audio_dir()
    src_path: Path = Path(file_path)
    dst_path: Path = Path.cwd() / AUDIO_FILE_DIR
    shutil.copytree(src=src_path, dst=dst_path)
    return True


def tarfile_pattern_match(file_path: str) -> Optional[Match[Any]]:
    """
    This function checks the given file is tar file or not with regex
    Args:
        file (str): file name to validate the file is tar file or not

    Returns:
        Match[str] | None: if pattern matches return matched pattern else None
    """
    return re.search(r"[a-zA-Z0-9_ -]+\.tgz$", file_path)


def fetch_audio_data(file_path_str: str) -> None:
    """
    This function recursively finds the tar fils and extract them into local audio directory
    Args:
        file_path_str (str): directory path to fetch all the audio files
    """
    file_path: Path = Path(file_path_str)
    for file in file_path.iterdir():
        if file.is_file():
            if tarfile_pattern_match(str(file)):
                extract_audio_files(file, State.delete_audio_folder)
                State.delete_audio_folder = False
        elif file.is_dir():
            fetch_audio_data(str(file))


def audio_pattern_match(file: str) -> Optional[Match[Any]]:
    """
    This function checks the given file is audio file or not with regex
    Args:
        file (str): file name to validate the file is audio file or not

    Returns:
        Match[str] | None: if pattern matches return matched patter else None
    """
    return re.search(r"[a-zA-Z0-9_-]+\.(opus|wav)$", file)


def filter_audio_data() -> None:
    """
    filter audio files from the local audio directory
    (some tar files contain other files along with audio files)
    """
    audio_path: Path = Path.cwd() / AUDIO_FILE_DIR
    for file in audio_path.iterdir():
        if not audio_pattern_match(str(file)):
            os.remove(file)


def load_data_recersively_from_folders(file_path_str: str) -> bool:
    """
    fetch audio files recursively from the given and filters the audio files

    file_path_str:
        file_path_str (str): source path to fetch audio files
    """
    fetch_audio_data(file_path_str)
    return True


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


def add_audio_files_with_regex(regex_str: str, path: Path) -> None:
    """
    Extract the compressed tgz files and add extracted files into local audio directory
    if and only if that compressed file match the given regex pattern

    Args:
        regex_str (str): regular expression string
        path (Path): file path
    """
    if path.is_file():
        if match_file_regex_pattern(regex_str, str(path)):
            extract_audio_files(path, State.delete_audio_folder)
            State.delete_audio_folder = False
    elif path.is_dir():
        for file in path.iterdir():
            add_audio_files_with_regex(regex_str, file)


def regex_to_path(regex_str: str) -> Path:
    """
    constructs the initial path (from here searching and regex validation starts)
    from the given regex

    Args:
        regex_str (str): regular expression string

    Returns:
        Path: inital Path to start search
    """
    path_split_list: List[str] = regex_str.split("/")
    path: PurePath = PurePath("/")
    for i in range(len(path_split_list) - 1):
        path_split_list[i] = path_split_list[i].strip("()*_- ")
        path = path.joinpath(path_split_list[i])
    return Path(path)


def load_data_with_regex(regex_str: str) -> bool:
    """
    Load and filter the audio files with regex pattern matching

    Args:
        regex_str (str): regular expression string

    Returns:
        bool: Return True if successfully loads the data else False
    """
    initial_path = regex_to_path(regex_str)
    add_audio_files_with_regex(regex_str, initial_path)
    return True
