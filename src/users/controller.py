from typing import Optional

from pymongo.collection import Collection
from functools import wraps
from bson import ObjectId

from database import mongodb_client
from users.models import User
from config import Config

users_collection: Collection = mongodb_client[Config.MONGO_DB_NAME].users


def validate_unique_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        email = kwargs.get("email")
        username = kwargs.get("username")
        if is_user_exist_by_username(username):
            raise ValueError("Username already exists.")
        if is_user_exist_by_email(email):
            raise ValueError("Email already exists.")
        res = func(*args, **kwargs)
        return res
    return wrapper


def insert_user(user: 'User', collection: Collection = users_collection):
    result = collection.insert_one(user.dict(exclude={"uid", }))
    user.uid = result.inserted_id
    return user


def update_user(user: 'User', collection: Collection = users_collection) -> 'User':
    obj = user.dict(exclude={"uid", "password"})
    collection.update_one({'_id': user.uid}, {"$set": obj})
    return user


def is_user_exist_by_email(email: str, collection=users_collection) -> bool:
    user = get_user_by_email(email, collection=collection)
    return bool(user)


def is_user_exist_by_username(username: str, collection=users_collection) -> bool:
    user = get_user_by_username(username, collection=collection)
    return bool(user)


def get_user_by_id(_id: ObjectId, collection=users_collection) -> Optional['User']:
    user = collection.find_one({"_id": _id})
    user = User.create_from_dict(**user) if user else None
    return user


def get_user_by_username(username: str, collection=users_collection) -> Optional['User']:
    user = collection.find_one({"username": username})
    return user


def get_user_by_email(email: str, collection=users_collection) -> 'User':
    user = collection.find_one({"email": email})
    user = User.create_from_dict(**user) if user else None
    return user


def login(email, password, collection=users_collection) -> Optional['User']:
    user = get_user_by_email(email=email, collection=collection)
    is_password_right = user.check_password(password=password, pwhash=user.password) if user else False
    if is_password_right:
        return user


def register(email, username, password, collection=users_collection) -> 'User':
    user = User.create_new(username=username, email=email, password=password)
    user = insert_user(user, collection=collection)
    return user

