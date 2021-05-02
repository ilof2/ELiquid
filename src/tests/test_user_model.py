from typing import Generator

from src.users.models import User


def test_user_create(user_dict):
    user = User.create(**user_dict)
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


def test_uid_is_mutable(user_dict):
    user = User.create(**user_dict)
    user_uid = user.uid
    from bson import ObjectId
    user._uid = ObjectId()
    assert user_uid != user.uid
