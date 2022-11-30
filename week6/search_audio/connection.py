"""
   Establish the connection to local elasticsearch cluster
"""
from elasticsearch import Elasticsearch

PASSWORD = "KH0rxvUZbE4jjOl95dIK"
USER = "elastic"
INDEX = "audio_files"
# creating a connection to elasticsearch cluster
client = Elasticsearch(
    "https://localhost:9200", http_auth=(USER, PASSWORD), verify_certs=False
)
