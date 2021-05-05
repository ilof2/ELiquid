from consumables.models import BaseConsumable


class Nicotine(BaseConsumable):
    vg: int
    pg: int
    strength: int

    @classmethod
    def create(cls, *args, **kwargs) -> 'Nicotine':
        uid = kwargs.pop("_id")
        new_class = cls(**kwargs)
        new_class.uid = uid
        return new_class
