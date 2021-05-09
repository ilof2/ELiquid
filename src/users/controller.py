from functools import wraps
from typing import Optional

from bson import ObjectId
from pymongo.collection import Collection

from database import mongo_connection
from signals import on_user_create
from users.models import User

users_collection_name = "users"
collection: Collection = getattr(mongo_connection, users_collection_name)


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


def insert_user(user: 'User'):
    result = collection.insert_one(user.dict(exclude={"uid", }))
    user.uid = result.inserted_id
    return user


def update_user(user: 'User') -> 'User':
    obj = user.dict(exclude={"uid", "password"})
    collection.update_one({'_id': user.uid}, {"$set": obj})
    return user


def is_user_exist_by_email(email: str) -> bool:
    user = get_user_by_email(email)
    return bool(user)


def is_user_exist_by_username(username: str) -> bool:
    user = get_user_by_username(username)
    return bool(user)


def get_user_by_id(_id: ObjectId) -> Optional['User']:
    user = collection.find_one({"_id": _id})
    user = User.create_from_dict_db(**user) if user else None
    return user


def get_user_by_username(username: str) -> Optional['User']:
    user = collection.find_one({"username": username})
    return user


def get_user_by_email(email: str) -> 'User':
    user = collection.find_one({"email": email})
    user = User.create_from_dict_db(**user) if user else None
    return user


def login(email, password) -> Optional['User']:
    user = get_user_by_email(email=email)
    is_password_right = user.check_password(password=password, pwhash=user.password) if user else False
    if is_password_right:
        return user


def register(email, username, password) -> 'User':
    user = User.create_new(username=username, email=email, password=password)
    user = insert_user(user)
    on_user_create.fire(user.uid)
    return user
