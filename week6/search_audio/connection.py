from elasticsearch import Elasticsearch
index = "audio_files"
# creating a connection to elasticsearch cluster
client = Elasticsearch(
    "https://localhost:9200",verify_certs=False
)
