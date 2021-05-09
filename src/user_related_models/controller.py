from bson import ObjectId
from pymongo.collection import Collection

from database import mongo_connection
from .models import UserInfo

collection: Collection = mongo_connection.user_info


def get_user_info(user_id: ObjectId):
    user_data: dict = collection.find_one({"user_id": user_id})
    if user_data:
        return UserInfo.create_from_db(**user_data)


def init_user_info(user_id: ObjectId):
    new_consumables = UserInfo(user_id=user_id)
    collection.insert_one(new_consumables.dict(by_alias=True))

