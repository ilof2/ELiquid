from typing import Generator, List

from bson import ObjectId

from database import mongodb_client
from users.models import User
from config import Config

users_conn = mongodb_client[Config.MONGO_DB_NAME].users


def insert_user(user: 'User'):
    result = users_conn.insert_one(user.dict())
    user.uid = result.inserted_id
    return user


def update_user(user: 'User') -> 'User':
    obj = user.dict(exclude={"uid", "password"})
    users_conn.update_one({'_id': user.uid}, {"$set": obj})
    return user


def update_users(users: List['User']):
    def return_user_as_dict(user):
        return user.dict(exclude={"uid", "password"})
    users_conn.update_many(map(return_user_as_dict, users))


def is_user_exist(_id: ObjectId) -> bool:
    user = get_user_by_id(_id)
    return bool(user)


def is_user_exist_by_email(email: str) -> bool:
    user = get_user_by_email(email)
    return bool(user)


def get_users() -> Generator:
    users: list = users_conn.find({})
    return User.create_from_list(users)


def get_user_by_id(_id: ObjectId) -> 'User' or None:
    user = users_conn.find_one({"_id": _id})
    user = User.create_from_dict(**user) if user else None
    return user


def get_user(user: 'User') -> 'User' or None:
    user = get_user_by_email(user.email)
    return user


def get_user_by_email(email: str) -> 'User':
    user = users_conn.find_one({"email": email})
    user = User.create_from_dict(**user)
    return user


def login(email, password) -> 'User' or None:
    user = get_user_by_email(email)
    if user.check_password(password=password, pwhash=user.password):
        return user
