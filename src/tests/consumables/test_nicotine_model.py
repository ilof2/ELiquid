from user_info.consumables import Nicotine


def nicotine_create(nicotine_dict_db):
    nicotine = Nicotine.create_from_db(**nicotine_dict_db)
    assert nicotine
    assert nicotine.strength == nicotine_dict_db['strength']
    assert nicotine.uid == nicotine_dict_db['_id']
    assert nicotine.pg == nicotine_dict_db['pg']
    assert nicotine.vg == nicotine_dict_db['vg']
    assert nicotine.amount == nicotine_dict_db['amount']
