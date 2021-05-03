from bson import ObjectId
from pymongo.database import Database
from pytest import fixture
from pymongo import MongoClient

from config import Config
from users import User


@fixture()
def user_dict():
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
def test_conn_to_db() -> Database:
    mongodb_client = MongoClient(Config.TEST_MONGO_URI, retryWrites=False)
    mongodb_conn = mongodb_client[Config.TEST_MONGO_DB_NAME]
    yield mongodb_conn
    mongodb_client.drop_database(Config.TEST_MONGO_DB_NAME)
    mongodb_client.close()
