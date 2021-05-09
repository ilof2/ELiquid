from bson import ObjectId
from pymongo.collection import Collection

from database import mongo_connection
from .models import UserInfo

collection: Collection = mongo_connection.user_info


def get_user_info(user_id: ObjectId):
    user_info: dict = collection.find_one({"user_id": user_id})
    if user_info:
        return UserInfo.create_from_db(**user_info)


def init_user_info(user_id: ObjectId):
    user_info = UserInfo(user_id=user_id)
    collection.insert_one(user_info.dict(by_alias=True))

