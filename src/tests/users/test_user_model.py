from typing import Generator

from users.models import User


def test_user_create(user_dict):
    user = User.create_new(**user_dict)
    assert user
    assert user.username == user_dict["username"]
    assert User.check_password(user.password, user_dict["password"])


def test_user_create_from_list(ten_users_generator):
    users_json_list = list(ten_users_generator)
    users = User.create_from_list(users_json_list)
    assert isinstance(users, Generator)
    users_list = list(users)
    assert len(users_list) == len(users_json_list)
    assert users_list[0].username == users_json_list[0]["username"]


def test_id_is_mutable(user_dict_db):
    user = User.create_from_dict(**user_dict_db)
    user_id = user.uid
    from bson import ObjectId
    user.uid = ObjectId()
    assert user_id != user.uid
