from .models import VG

from config import Config
from database import mongodb_client

db_vg_connection = mongodb_client[Config.MONGO_DB_NAME].vg


def insert_vg_one(vg: 'VG', vg_conn=db_vg_connection):
    result = vg_conn.insert_one(vg.dict())
    vg._cid = result.inserted_id
    return vg


def update_vg_one(vg: 'VG', vg_conn=db_vg_connection):
    vg_conn.update_one({'_id': vg.uid}, {"$set": vg.dict()})
    return vg
