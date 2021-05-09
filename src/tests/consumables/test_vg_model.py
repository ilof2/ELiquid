from user_info.consumables import VG


def test_vg_from_db(vg_dict_db):
    vg = VG.create_from_db(**vg_dict_db)
    assert vg.amount == vg_dict_db['amount']
    assert vg.uid == vg_dict_db['_id']
