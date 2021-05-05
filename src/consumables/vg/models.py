from ..models import BaseConsumable


class VG(BaseConsumable):

    @classmethod
    def create(cls, *args, **kwargs) -> 'VG':
        uid = kwargs.pop("_id")
        new_class = cls(**kwargs)
        new_class.uid = uid
        return new_class
