from typing import Generator, List

from bson import ObjectId

from app import db
from users.models import User


def insert_user(user: 'User'):
    result = db.users.insert_one(user.dict())
    user._uid = result.inserted_id
    return user


def update_user(user: 'User') -> 'User':
    db.users.update_one({'_id': user.uid}, {"$set": user.dict()})
    return user


def update_users(users: List['User']):
    db.users.update_many(users)


def update_or_create_user(user: 'User') -> 'User':
    if is_user_exist(user.uid):
        return update_user(user)
    return insert_user(user)


def is_user_exist(uid: ObjectId) -> bool:
    user = get_user(uid)
    return bool(user)


def get_users() -> Generator:
    users = db.users.find({})
    return User.create_from_list(users)


def get_user(uid: ObjectId) -> 'User' or None:
    user = db.users.find_one({"_id": uid})
    user = User.create(**user) if user else None
    return user
