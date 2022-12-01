"""
This module provide functionalities to add, search files from elasticsearch
"""
from pathlib import Path
from typing import Any, List

from elastic_transport import ObjectApiResponse

from connection import client
from constants import AUDIO_FILE_DIR, INDEX, TEMP_AUDIO_DIR


def is_document_exists(document_name: str) -> List[str]:
    """
    check whether a document exists in the elasticsearch cluster or not,
    if exists it returns the list of documents that are exists with given document name
    Args:
        document_name (str): document name to search

    Returns:
        List[str]: list of documents
    """
    res = client.search(
        index=INDEX,
        query={"match": {"audio_name": {"query": document_name, "fuzziness": "AUTO"}}},
    )
    return res["hits"]["hits"]


def create_index():
    """
    creates an index in the local elastic search cluster
    """
    client.indices.create(index=INDEX, ignore=400)


def add_document(doc: dict) -> None:
    """
    Adds the individual document to the elasticsearch cluster index

    Args:
        doc (dict): Document to add into the index
    """
    client.index(index=INDEX, document=doc)


def add_all_data() -> bool:
    """
    Adds all the data from local temp folder to the elasticsearch cluster index
    """
    path: Path = Path.cwd() / TEMP_AUDIO_DIR
    for audio in path.iterdir():

        is_document = is_document_exists(((audio.name).split("."))[0])
        if len(is_document) == 0:

            doc: dict = {
                "audio_name": ((audio.name).split("."))[0],
                "audio_path": AUDIO_FILE_DIR + "/" + audio.name,
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
        query={"match": {"audio_name": {"query": name, "fuzziness": "AUTO"}}},
    )
    matched_audios: List[str] = []
    for file in response["hits"]["hits"]:
        audio = file["_source"]["audio_path"]
        matched_audios.append(audio)
    return matched_audios
