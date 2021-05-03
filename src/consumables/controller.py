from app import db
from consumables.models import Nicotine, Flavor, PG, VG

nicotine_conn = db.nicotine
flavor_conn = db.flavor
pg_conn = db.pg
vg_conn = db.vg


def insert_nicotine_one(nicotine: 'Nicotine'):
    result = nicotine_conn.insert_one(nicotine.dict())
    nicotine._cid = result.inserted_id
    return nicotine


def insert_flavor_one(flavor: 'Flavor'):
    result = flavor_conn.insert_one(flavor.dict())
    flavor._cid = result.inserted_id
    return flavor


def insert_pg_one(pg: 'PG'):
    result = pg_conn.insert_one(pg.dict())
    pg._cid = result.inserted_id
    return pg


def insert_vg_one(vg: 'VG'):
    result = vg_conn.insert_one(vg.dict())
    vg._cid = result.inserted_id
    return vg

def insert_vg_many(vg: 'VG'):
    result = vg_conn.insert_many(vg.dict())
    vg._cid = result.

