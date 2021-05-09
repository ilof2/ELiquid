from typing import List

from bson import ObjectId
from pydantic import BaseModel, Field, parse_obj_as

from user_related_models.consumables.enums import FlavorType


class Nicotine(BaseModel):
    uid: ObjectId = Field(default_factory=lambda: ObjectId(), alias="_id")
    amount: int = 0
    name: str = Field(min_length=1, max_length=200)
    vg: int
    pg: int
    strength: int

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def create_from_db(cls, **kwargs) -> 'Nicotine':
        return cls(**kwargs)

    @classmethod
    def create_new(cls, **kwargs) -> 'Nicotine':
        new_class = cls(**kwargs)
        new_class.uid = ObjectId()
        return new_class

    @classmethod
    def create_from_list_db(cls, data_list):
        return parse_obj_as(List[cls], data_list)


class Flavor(BaseModel):
    uid: ObjectId = Field(default_factory=lambda: ObjectId(), alias="_id")
    amount: int = Field(ge=0)
    name: str = Field(min_length=1, max_length=200)
    flavor_type: FlavorType

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def create_from_db(cls, **kwargs) -> 'Flavor':
        new_class = cls(**kwargs)
        return new_class

    @classmethod
    def create_new(cls, **kwargs):
        new_class = cls(**kwargs)
        new_class.name = new_class.name.strip()
        new_class.uid = ObjectId()
        return new_class

    @classmethod
    def create_from_list_db(cls, data_list):
        return parse_obj_as(List[cls], data_list)


class PG(BaseModel):
    uid: ObjectId = Field(default_factory=lambda: ObjectId(), alias="_id")
    amount: int = 0

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def create_from_db(cls, **kwargs) -> 'PG':
        return cls(**kwargs)

    @classmethod
    def create_new(cls, **kwargs) -> 'PG':
        new_class = cls(**kwargs)
        new_class.uid = ObjectId()
        return new_class


class VG(BaseModel):
    uid: ObjectId = Field(default_factory=lambda: ObjectId(), alias="_id")
    amount: int = 0

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def create_from_db(cls, **kwargs) -> 'VG':
        return cls(**kwargs)

    @classmethod
    def create_new(cls, **kwargs) -> 'VG':
        new_class = cls(**kwargs)
        new_class.uid = ObjectId()
        return new_class


class Consumables(BaseModel):
    vg: VG = VG()
    pg: PG = PG()
    nicotine: List[Nicotine] = []
    flavor: List[Flavor] = []

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def create_from_db(cls, **kwargs):
        vg_dict = kwargs.get("vg")
        pg_dict = kwargs.get("pg")
        nicotine_list = kwargs.get("nicotine")
        flavor_list = kwargs.get("flavor")
        vg: VG = VG.create_from_db(**vg_dict)
        pg: PG = PG.create_from_db(**pg_dict)
        nicotine_list: List[Nicotine] = Nicotine.create_from_list_db(nicotine_list)
        flavor_list: List[Flavor] = Flavor.create_from_list_db(flavor_list)
        cls(vg=vg, pg=pg, nicotine=nicotine_list, flavor=flavor_list, )

    @classmethod
    def create_new(cls):
        return cls()

    @classmethod
    def create_from_list(cls, data_list: List[dict]):
        return [Consumables.create_from_db(**consumable) for consumable in data_list]
