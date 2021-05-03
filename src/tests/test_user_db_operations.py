from pymongo.database import Database

from users import User
from users.contoller import insert_user, get_user


def test_user_create(test_conn_to_db: Database, user_dict):
    users_collection = test_conn_to_db.users
    user = User.create_new(**user_dict)
    inserted_user = insert_user(user, users_conn=users_collection)
    assert inserted_user.username == user_dict["username"]
    user_from_db = users_collection.find_one({"username": user_dict["username"]})
    user_from_db = User.create_from_dict(**user_from_db)
    assert user_from_db.uid == inserted_user.uid


def test_user_get(test_conn_to_db: Database, user_dict):
    users_collection = test_conn_to_db.users
    user = User.create_new(**user_dict)
    inserted_user = insert_user(user, users_conn=users_collection)
    user_from_db = get_user(inserted_user, users_collection)
    assert user_from_db
    assert user_from_db.email == user_dict["email"]
