from .models import Nicotine
from typing import List

from config import Config
from database import mongodb_client


nicotine_conn = mongodb_client[Config.MONGO_DB_NAME].nicotine


def insert_nicotine_one(nicotine: 'Nicotine'):
    result = nicotine_conn.insert_one(nicotine.dict())
    nicotine.uid = result.inserted_id
    return nicotine


def insert_nicotine_many(nicotine: 'Nicotine'):
    result = nicotine_conn.insert_many(nicotine.dict())
    nicotine.uid = result.inserted_id
    return nicotine


def update_nicotine_one(nicotine: 'Nicotine'):
    nicotine_conn.update_one({'_id': nicotine.uid}, {"$set": nicotine.dict()})
    return nicotine

