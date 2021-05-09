from user_related_models.consumables.models import Flavor


def test_flavor_create_from_db(flavor_dict_db):
    flavor = Flavor.create_from_db(**flavor_dict_db)
    assert flavor
    assert flavor.name == flavor_dict_db['name'].strip()
    assert flavor.uid == flavor_dict_db['_id']
    assert flavor.flavor_type.value == flavor_dict_db['flavor_type'].strip()
    assert flavor.amount == flavor_dict_db['amount']
