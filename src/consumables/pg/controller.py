from .models import PG

from config import Config
from database import mongodb_client

db_pg_connection = mongodb_client[Config.MONGO_DB_NAME].pg


def insert_pg_one(pg: 'PG', pg_conn=db_pg_connection):
    result = pg_conn.insert_one(pg.dict())
    pg.uid = result.inserted_id
    return pg


def update_pg_one(pg: 'PG', pg_conn=db_pg_connection):
    pg_conn.update_one({'_id': pg.uid}, {"$set": pg.dict()})
    return pg
