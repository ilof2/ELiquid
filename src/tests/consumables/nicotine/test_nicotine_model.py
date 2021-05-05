from consumables.nicotine.models import Nicotine


def nicotine_create(nicotine_dict):
    nicotine = Nicotine.create(**nicotine_dict)
    assert nicotine
    assert nicotine.strength == nicotine_dict['strength']
    assert nicotine.uid == nicotine_dict['_id']
    assert nicotine.pg == nicotine_dict['pg']
    assert nicotine.vg == nicotine_dict['vg']
    assert nicotine.amount == nicotine.dict['amount']
    assert nicotine.consumable_type == ['consumable_type']
