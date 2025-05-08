
# Chapter 13: Search & Filtering with Elasticsearch

# Example of integrating Elasticsearch with Django
from elasticsearch_dsl import Document, Text, Date
from elasticsearch_dsl.connections import connections

connections.create_connection()

class ProductDocument(Document):
    name = Text()
    description = Text()
    created_at = Date()

    class Index:
        name = 'products'
    