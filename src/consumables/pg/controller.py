from .models import PG
from typing import List

from config import Config
from database import mongodb_client

pg_conn = mongodb_client[Config.MONGO_DB_NAME].pg


def insert_pg_one(pg: 'PG'):
    result = pg_conn.insert_one(pg.dict())
    pg.uid = result.inserted_id
    return pg


def update_pg_one(pg: 'PG'):
    pg_conn.update_one({'_id': pg.uid}, {"$set": pg.dict()})
    return pg
