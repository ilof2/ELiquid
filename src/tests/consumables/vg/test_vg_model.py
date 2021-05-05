from consumables.vg.models import VG


def test_vg_models(vg_dict):
    vg = VG.create(**vg_dict)
    assert vg.consumable_type == vg_dict['consumable_type']
    assert vg.amount == vg_dict['amount']
    assert vg.uid == vg_dict['_id']