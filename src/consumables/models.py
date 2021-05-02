from pydantic import BaseModel, validator
from bson import ObjectId


class BaseConsumable(BaseModel):
    _id: ObjectId = ObjectId()
    type: str
    amount: int = 0


class Nicotine(BaseConsumable):
    vg: int
    pg: int
    strength: int


class Flavor(BaseConsumable):
    name: str
    flavorType: str


class VG(BaseConsumable):
    pass


class PG(BaseConsumable):
    pass
