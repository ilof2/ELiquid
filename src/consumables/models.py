from pydantic import BaseModel, validator, PrivateAttr
from bson import ObjectId


class BaseConsumable(BaseModel):
    _cid: ObjectId = PrivateAttr(default_factory=lambda: ObjectId())
    consumable_type: str
    amount: int = 0

    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, val):
        if isinstance(val, ObjectId):
            self._cid = val


class Nicotine(BaseConsumable):
    vg: int
    pg: int
    strength: int

    @classmethod
    def create(cls, *args, **kwargs):
        cid = kwargs.pop("_id")
        new_class = cls(**kwargs)
        new_class._cid = cid
        return new_class


class Flavor(BaseConsumable):
    name: str
    flavorType: str

    @classmethod
    def create(cls, *args, **kwargs):
        cid = kwargs.pop("_id")
        new_class = cls(**kwargs)
        new_class._cid = cid
        return new_class


class VG(BaseConsumable):

    @classmethod
    def create(cls, *args, **kwargs):
        cid = kwargs.pop("_id")
        new_class = cls(**kwargs)
        new_class._cid = cid
        return new_class


class PG(BaseConsumable):

    @classmethod
    def create(cls, *args, **kwargs):
        cid = kwargs.pop("_id")
        new_class = cls(**kwargs)
        new_class._cid = cid
        return new_class

