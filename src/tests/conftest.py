from bson import ObjectId
from pymongo.database import Database
from pytest import fixture
from pymongo import MongoClient

from config import Config
from user_related_models.consumables.enums import FlavorType
from users import User


@fixture()
def user_dict():
    obj = {
        "username": "test",
        "password": "123",
        "email": "test@test.com",
    }
    return obj


@fixture()
def user_dict_db():
    obj = {
        "_id": ObjectId(),
        "username": "test",
        "password": "123",
        "email": "test@test.com",
    }
    return obj


@fixture()
def user_obj(user_dict: dict) -> User:
    return User.create_new(**user_dict)


@fixture()
def ten_users_generator():
    def users():
        for name_num in range(10):
            obj = {
                "_id": ObjectId(),
                "username": f"test{name_num}",
                "password": "123",
                "email": f"test{name_num}@test.comm",
            }
            yield obj
    return users()


@fixture()
def flavor_dict():
    flavor_dict = {
        "flavor_type": "strawberry",
        "amount": 250,
        "name": "MantAna",
    }
    return flavor_dict


@fixture()
def flavor_dict_db():
    flavor_dict = {
        "uid": ObjectId(),
        "amount": 250,
        "name": "Melon",
        "flavor_type": FlavorType.VG.value
    }
    return flavor_dict


@fixture()
def nicotine_dict():
    nicotine_dict = {
        "amount": 250,
        "name": "test",
        "pg": 40,
        "vg": 60,
        "strength": 18,
    }
    return nicotine_dict


@fixture()
def nicotine_dict_db():
    nicotine_dict = {
        "uid": ObjectId(),
        "amount": 250,
        "name": "test",
        "pg": 40,
        "vg": 60,
        "strength": 18,
    }
    return nicotine_dict


@fixture()
def vg_dict():
    vg_dict = {
        "amount": 112,
    }
    return vg_dict


@fixture()
def vg_dict_db():
    vg_dict = {
        "uid": ObjectId(),
        "amount": 112,
    }
    return vg_dict


@fixture()
def pg_dict():
    pg_dict = {
        "amount": 95,
    }
    return pg_dict


@fixture()
def pg_dict_db():
    pg_dict = {
        "uid": ObjectId(),
        "amount": 95,
    }
    return pg_dict


@fixture()
def test_conn_to_db() -> Database:
    mongodb_client = MongoClient(Config.TEST_MONGO_URI, retryWrites=False)
    mongodb_conn = mongodb_client[Config.TEST_MONGO_DB_NAME]
    yield mongodb_conn
    mongodb_client.drop_database(Config.TEST_MONGO_DB_NAME)
    mongodb_client.close()
