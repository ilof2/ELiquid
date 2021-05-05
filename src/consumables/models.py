from pydantic import BaseModel, Field
from bson import ObjectId


class BaseConsumable(BaseModel):
    uid: ObjectId = Field(default_factory=lambda: ObjectId())
    consumable_type: str
    amount: int = 0

    class Config:
        arbitrary_types_allowed = True
