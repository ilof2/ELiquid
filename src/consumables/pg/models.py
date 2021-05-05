from ..models import BaseConsumable


class PG(BaseConsumable):

    @classmethod
    def create(cls, *args, **kwargs) -> 'PG':
        uid = kwargs.pop("_id")
        new_class = cls(**kwargs)
        new_class.uid = uid
        return new_class
