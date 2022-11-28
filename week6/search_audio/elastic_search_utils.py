from pathlib import Path
from elastic_transport import ObjectApiResponse
from typing import List
from connection import client, index
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
AUDIO_FILE_DIR = "audio"
# creates an index if not alread exists
def create_index():
    """
    creates an index in the local elastic search cluster
    """
    client.indices.create(index=index)


def add_document(doc: dict) -> None:
    """
    Adds the individual document to the index

    Args:
        doc (dict): Document to add to the index
    """
    client.index(index=index, body=doc)


def add_all_data() -> None:
    """
    Adds all the data from local audio folder to the index
    """
    if client.indices.exists(index=index):
        client.indices.delete(index=index)
    if not client.indices.exists(index=index):
        create_index()
    path:Path = Path.cwd() / AUDIO_FILE_DIR
    for audio in path.iterdir():
        doc: dict = {
            "audio_name": ((audio.name).split("."))[0],
            "audio_path": str(audio),
        }
        add_document(doc=doc)


def get_audio_file_path(name: str) -> List[str]:
    """
    Takes the audio file name as input and returns the list of audio file paths if they exists else empty list

    Args:
        name (str): audio file name

    Returns:
        str: audio path
    """
    res: ObjectApiResponse = client.search(
        index=index,
        body={"query": {"match": {"audio_name": {"query": name, "fuzziness": "AUTO"}}}},
    )
    matched_audios:List[str] = []
    for file in res["hits"]["hits"]:
        audio = file["_source"]["audio_path"]
        matched_audios.append(audio)
    return matched_audios
