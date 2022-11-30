"""
This module provide functionalities to add, search files from elasticsearch
"""
from pathlib import Path
from typing import Any, List

from elastic_transport import ObjectApiResponse

from connection import INDEX, client
from utils import AUDIO_FILE_DIR


# creates an index if not alread exists
def create_index():
    """
    creates an index in the local elastic search cluster
    """
    client.indices.create(index=INDEX)


def add_document(doc: dict) -> None:
    """
    Adds the individual document to the elasticsearch cluster index

    Args:
        doc (dict): Document to add into the index
    """
    client.index(index=INDEX, document=doc)


def add_all_data() -> bool:
    """
    Adds all the data from local audio folder to the elasticsearch cluster index
    """
    if client.indices.exists(index=INDEX):
        client.indices.delete(index=INDEX)
    if not client.indices.exists(index=INDEX):
        create_index()
    path: Path = Path.cwd() / AUDIO_FILE_DIR
    for audio in path.iterdir():
        doc: dict = {
            "audio_name": ((audio.name).split("."))[0],
            "audio_path": str(audio),
        }
        add_document(doc=doc)
    return True


def get_audio_file_path(name: str) -> List[str]:
    """
    Takes the audio file name as input and returns the list of audio file paths
    if they exists else empty list

    Args:
        name (str): audio file name

    Returns:
        str: audio path
    """
    response: ObjectApiResponse[Any] = client.search(
        index=INDEX,
        body={"query": {"match": {"audio_name": {"query": name, "fuzziness": "AUTO"}}}},
    )
    matched_audios: List[str] = []
    for file in response["hits"]["hits"]:
        audio = file["_source"]["audio_path"]
        matched_audios.append(audio)
    return matched_audios
