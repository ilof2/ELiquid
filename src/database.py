from pymongo import MongoClient

from config import Config

mongodb_client = MongoClient(Config.MONGO_DB_URI, retryWrites=False)
