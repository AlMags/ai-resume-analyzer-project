from pymongo import MongoClient

from app.config import (
    get_mongodb_database, 
    get_mongodb_uri,
)

def get_client():
    return MongoClient(get_mongodb_uri())

def get_database():
    client = get_client()

    return client[get_mongodb_database()]