from ..models import BaseConsumable


class Flavor(BaseConsumable):
    name: str
    flavor_type: str

    @classmethod
    def create(cls, *args, **kwargs) -> 'Flavor':
        uid = kwargs.pop("_id")
        new_class = cls(**kwargs)
        new_class.uid = uid
        new_class.flavor_type = new_class.flavor_type.strip()
        new_class.name = new_class.name.strip()
        return new_class
