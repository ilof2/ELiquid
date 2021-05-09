from bson import ObjectId
from pydantic import BaseModel, parse_obj_as

from user_related_models.consumables.models import Consumables


class UserInfo(BaseModel):
    user_id: ObjectId
    consumables: Consumables = Consumables.create_new()

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def create_from_db(cls, **kwargs) -> 'UserInfo':
        return parse_obj_as(UserInfo, kwargs)
