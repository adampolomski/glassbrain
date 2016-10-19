from pymongo import MongoClient
import os

def getDb():
    client = MongoClient(os.environ.get('MONGODB_URI', "mongodb://localhost"))
    return client.get_default_database()