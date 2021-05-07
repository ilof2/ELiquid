from pymongo.database import Database

from users import User
from users.controller import insert_user, get_user_by_id, get_user_by_email, login, update_user


def test_user_create(test_conn_to_db: Database, user_obj: User):
    users_collection = test_conn_to_db.users
    inserted_user = insert_user(user_obj, collection=users_collection)
    assert inserted_user.username == user_obj.username
    user_from_db = users_collection.find_one({"username": user_obj.username})
    user_from_db = User.create_from_dict(**user_from_db)
    assert user_from_db.uid == inserted_user.uid


def test_user_get(test_conn_to_db: Database, user_obj: User):
    users_collection = test_conn_to_db.users
    inserted_user = insert_user(user_obj, collection=users_collection)
    user_from_db = get_user_by_id(inserted_user.uid, collection=users_collection)
    assert user_from_db
    assert user_from_db.email == user_obj.email


def test_user_by_id(test_conn_to_db: Database, user_obj: User):
    users_collection = test_conn_to_db.users
    insert_user(user_obj, collection=users_collection)
    user_from_db = get_user_by_id(user_obj.uid, collection=users_collection)
    assert user_from_db
    assert user_from_db.username == user_obj.username
    assert user_from_db.uid == user_obj.uid


def test_user_by_email(test_conn_to_db: Database, user_obj: User):
    users_collection = test_conn_to_db.users
    insert_user(user_obj, collection=users_collection)
    user_from_db = get_user_by_email(user_obj.email, collection=users_collection)
    assert user_from_db
    assert user_from_db.username == user_obj.username
    assert user_from_db.uid == user_obj.uid


def test_login(test_conn_to_db: Database, user_obj: User):
    users_collection = test_conn_to_db.users
    insert_user(user_obj, collection=users_collection)
    user = login(email=user_obj.email, password="123", collection=users_collection)
    assert user
    assert user.email == user_obj.email
    assert user.uid == user_obj.uid


def test_update_user(test_conn_to_db: Database, user_obj: User):
    users_collection = test_conn_to_db.users
    insert_user(user_obj, collection=users_collection)
    user_in_db = get_user_by_email(user_obj.email, collection=users_collection)
    assert user_in_db.username == user_obj.username
    user_obj.username = "test_changed"
    assert user_in_db.username != user_obj.username
    update_user(user_obj, collection=users_collection)
    user_in_db = get_user_by_email(user_obj.email, collection=users_collection)
    assert user_in_db.username == user_obj.username == "test_changed"
    assert user_obj.uid == user_in_db.uid
