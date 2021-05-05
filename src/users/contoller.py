from pymongo.collection import Collection

from bson import ObjectId

from database import mongodb_client
from users.models import User
from config import Config

conn: Collection = mongodb_client[Config.MONGO_DB_NAME].users


def insert_user(user: 'User', users_conn: Collection = conn):
    result = users_conn.insert_one(user.dict(exclude={"uid", }))
    user.uid = result.inserted_id
    return user


def update_user(user: 'User', users_conn: Collection = conn) -> 'User':
    obj = user.dict(exclude={"uid", "password"})
    users_conn.update_one({'_id': user.uid}, {"$set": obj})
    return user


def is_user_exist(_id: ObjectId) -> bool:
    user = get_user_by_id(_id)
    return bool(user)


def is_user_exist_by_email(email: str) -> bool:
    user = get_user_by_email(email)
    return bool(user)


def get_user_by_id(_id: ObjectId, users_conn=conn) -> 'User' or None:
    user = users_conn.find_one({"_id": _id})
    user = User.create_from_dict(**user) if user else None
    return user


def get_user(user: 'User', users_conn=conn) -> 'User' or None:
    user = get_user_by_email(email=user.email, users_conn=users_conn)
    return user


def get_user_by_email(email: str, users_conn=conn) -> 'User':
    user = users_conn.find_one({"email": email})
    user = User.create_from_dict(**user) if user else None
    return user


def login(email, password, users_conn=conn) -> 'User' or None:
    user = get_user_by_email(email=email, users_conn=users_conn)
    is_password_right = user.check_password(password=password, pwhash=user.password) if user else False
    if is_password_right:
        return user


def register(email, username, password, users_conn=conn) -> 'User':
    user = User.create_new(username=username, email=email, password=password)
    user = insert_user(user, users_conn=users_conn)
    return user

