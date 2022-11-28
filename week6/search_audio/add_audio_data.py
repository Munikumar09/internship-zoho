from pathlib import Path
import tarfile
from tarfile import TarFile
import shutil
import re
from re import Match
from elastic_search_utils import AUDIO_FILE_DIR
import os

global DELETE_EXISTING_AUDIO_DIR
DELETE_EXISTING_AUDIO_DIR = True


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
    Extract the audio files from provided file path and stores all the extracted audio files in local audio directory

    Args:
        file_path (Path): file path to extract audio files from
        delete_existing_dir (bool, optional): deletes the local audio directory if exits. Defaults to True.

    Returns:
        bool: return True if successfully audio files were extracted
    """
    if delete_existing_dir:
        delete_existing_audio_dir()
    tar_file: TarFile = tarfile.open(file_path)
    try:
        tar_file.extractall(f"./{AUDIO_FILE_DIR}")
    except Exception as e:
        print(e)
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


def tarfile_pattern_match(file_path: str) -> (Match[str] | None):
    """
    This function checks the given file is tar file or not with regex
    Args:
        file (str): file name to validate the file is tar file or not

    Returns:
        Match[str] | None: if pattern matches return matched pattern else None
    """
    return re.search("[a-zA-Z0-9_ -].tgz$", file_path)


def fetch_audio_data(file_path_str: str):
    """
    This function recursively finds the tar fils and extract them into local audio directory
    Args:
        file_path_str (str): directory path to fetch all the audio files
    """
    file_path: Path = Path(file_path_str)
    for file in file_path.iterdir():
        if file.is_file():
            if tarfile_pattern_match(str(file)):
                global DELETE_EXISTING_AUDIO_DIR
                extract_audio_files(file, DELETE_EXISTING_AUDIO_DIR)
                DELETE_EXISTING_AUDIO_DIR = False
        elif file.is_dir():
            fetch_audio_data(str(file))


def audio_pattern_match(file: str) -> (Match[str] | None):
    """
    This function checks the given file is audio file or not with regex
    Args:
        file (str): file name to validate the file is audio file or not

    Returns:
        Match[str] | None: if pattern matches return matched patter else None
    """
    return re.search("[a-zA-Z0-9_]\.(opus|wav)$", file)


def filter_audio_data() -> None:
    """
    filter audio files from the local audio directory(some tar files contain other files along with audio files)
    """
    audio_path: Path = Path.cwd() / AUDIO_FILE_DIR
    for file in audio_path.iterdir():
        if not audio_pattern_match(str(file)):
            os.remove(file)


def load_data(file_path_str: str):
    """
    fetch audio files recursively from the given and filters the audio files

    file_path_str:
        file_path_str (str): source path to fetch audio files
    """
    fetch_audio_data(file_path_str)
    filter_audio_data()
