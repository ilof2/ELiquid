from bson import ObjectId
from pytest import fixture


@fixture()
def user_dict():
    obj = {
        "_id": ObjectId(),
        "username": "test",
        "password": "123",
        "email": "test@test.com",
    }
    return obj


@fixture()
def ten_users_generator():
    def users():
        for name_num in range(10):
            obj = {
                "_id": ObjectId(),
                "username": f"test{name_num}",
                "password": "123",
                "email": f"test{name_num}@test.comm",
            }
            yield obj
    return users()


@fixture()
def flavor_dict():
    flavor_dict = {
        "_id": ObjectId(),
        "consumable_type": "flavors",
        "flavor_type": "strawberry",
        "amount": 250,
        "name": "MantAna",
    }
    return flavor_dict


@fixture()
def nicotine_dict():
    nicotine_dict = {
        "_id": ObjectId(),
        "amount": 250,
        "pg": 40,
        "vg": 60,
        "strength": 18,
        "consumable_type": "nicotine"

    }
    return nicotine_dict


@fixture()
def vg_dict():
    vg_dict = {
        "_id": ObjectId(),
        "amount": 112,
        "consumable_type": "vg"

    }
    return vg_dict


@fixture()
def pg_dict():
    pg_dict = {
        "_id": ObjectId(),
        "amount": 95,
        "consumable_type": "pg"
    }
    return pg_dict
