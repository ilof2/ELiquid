import os

from pymongo import MongoClient

from config import Config

mongodb_client = MongoClient(Config.MONGO_DB_URI, retryWrites=False)
mongo_connection = mongodb_client[Config.MONGO_DB_NAME]

if os.environ.get("PYTEST_RUN_CONFIG"):
    mongo_connection = mongodb_client[Config.TEST_MONGO_DB_NAME]
