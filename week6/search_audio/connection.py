from elasticsearch import Elasticsearch
PASSWORD = "mYcJTKtyoGJacEN3kamj"
USER = "elastic"
index = "audio_files"
# creating a connection to elasticsearch cluster
client = Elasticsearch(
    "https://localhost:9200", basic_auth=(USER, PASSWORD), verify_certs=False
)
