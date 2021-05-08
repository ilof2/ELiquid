from bson import ObjectId
from pydantic import BaseModel

from user_related_models.consumables.models import Consumables


class UserRelatedModels(BaseModel):
    user_id: ObjectId = None
    consumables: Consumables
