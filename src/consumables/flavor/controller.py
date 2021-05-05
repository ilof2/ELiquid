from .models import Flavor

from config import Config
from database import mongodb_client


db_flavor_connection = mongodb_client[Config.MONGO_DB_NAME].flavor


def insert_flavor_one(flavor: 'Flavor', flavor_conn=db_flavor_connection):
    result = flavor_conn.insert_one(flavor.dict())
    flavor.uid = result.inserted_id
    return flavor


def insert_flavor_many(flavor: 'Flavor', flavor_conn=db_flavor_connection):
    result = flavor_conn.insert_many(flavor.dict())
    flavor.uid = result.inserted_id
    return flavor


def update_flavor_one(flavor: 'Flavor', flavor_conn=db_flavor_connection):
    flavor_conn.update_one({'_id': flavor.uid}, {"$set": flavor.dict()})
    return flavor
