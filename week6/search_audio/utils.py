from pathlib import Path

from elastic_transport import ObjectApiResponse

from connection import client, index

# creates an index if not alread exists
if not client.indices.exists(index=index):
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
    Adds all the data from audio folder to the index
    """
    path = Path.cwd() / "audio"
    for audio in path.iterdir():
        doc: dict = {"name": ((audio.name).split("."))[0], "audio": str(audio)}
        add_document(doc=doc)


def get_audio_file_path(name: str) -> str:
    """
    Takes the audio file name as input and retuens the path to that audio file if it exists else empty stringf

    Args:
        name (str): audio name

    Returns:
        str: audio path
    """
    res: ObjectApiResponse = client.search(
        index=index, body={"query": {"match": {"name": name}}}
    )
    if res["hits"]["hits"]:
        return res["hits"]["hits"][0]["_source"]["audio"]
    return ""
