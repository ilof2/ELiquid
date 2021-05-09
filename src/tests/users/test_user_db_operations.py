from pymongo.database import Database

from users import User
from users.controller import insert_user, get_user_by_id, get_user_by_email, login, update_user


def test_user_create(test_conn_to_db: Database, user_obj: User):
    inserted_user = insert_user(user_obj)
    assert inserted_user.username == user_obj.username
    user_from_db = test_conn_to_db.users.find_one({"username": user_obj.username})
    user_from_db = User.create_from_dict_db(**user_from_db)
    assert user_from_db.uid == inserted_user.uid


def test_user_get(user_obj: User):
    inserted_user = insert_user(user_obj)
    user_from_db = get_user_by_id(inserted_user.uid)
    assert user_from_db
    assert user_from_db.email == user_obj.email


def test_user_by_id(user_obj: User):
    insert_user(user_obj)
    user_from_db = get_user_by_id(user_obj.uid)
    assert user_from_db
    assert user_from_db.username == user_obj.username
    assert user_from_db.uid == user_obj.uid


def test_user_by_email(user_obj: User):
    insert_user(user_obj)
    user_from_db = get_user_by_email(user_obj.email)
    assert user_from_db
    assert user_from_db.username == user_obj.username
    assert user_from_db.uid == user_obj.uid


def test_login(user_obj: User):
    insert_user(user_obj)
    user = login(email=user_obj.email, password="123")
    assert user
    assert user.email == user_obj.email
    assert user.uid == user_obj.uid


def test_update_user(user_obj: User):
    insert_user(user_obj)
    user_in_db = get_user_by_email(user_obj.email)
    assert user_in_db.username == user_obj.username
    user_obj.username = "test_changed"
    assert user_in_db.username != user_obj.username
    update_user(user_obj)
    user_in_db = get_user_by_email(user_obj.email)
    assert user_in_db.username == user_obj.username == "test_changed"
    assert user_obj.uid == user_in_db.uid
