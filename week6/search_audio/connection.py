"""
   Establish the connection to local elasticsearch cluster
"""
from elasticsearch import Elasticsearch

from constants import PASSWORD, USER

# creating a connection to elasticsearch cluster
client = Elasticsearch(
    "https://localhost:9200", http_auth=(USER, PASSWORD), verify_certs=False
)
