"""
provide utility members
"""
AUDIO_FILE_DIR = "audio"
# pylint: disable=R0903


class State:
    """
    This class is for storing static variable for various purposes like
    preventing the data tobe reloaded when page reloaded
    Attributes:
    audio_files_loaded(bool): To ensure audio files are loaded and avoid reloading
    files_added_to_elastcsearch(bool): To ensure file names and paths are added to elasticsearch
                                       cluster and avoid adding again
    delete_audio_folder(bool): While adding audio files this variable indicates whether the existing
                              audio folder would have to be deleted or not
    """

    audio_files_loaded = False
    files_added_to_elastcsearch = False
    delete_audio_folder = True
