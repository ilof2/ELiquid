from consumables.flavor.models import Flavor


def test_flavor_create(flavor_dict):
    flavor = Flavor.create(**flavor_dict)
    assert flavor
    assert flavor.name == flavor_dict['name'].strip()
    assert flavor.uid == flavor_dict['_id']
    assert flavor.flavor_type == flavor_dict['flavor_type'].strip()
    assert flavor.consumable_type == flavor_dict['consumable_type']
    assert flavor.amount == flavor_dict['amount']

