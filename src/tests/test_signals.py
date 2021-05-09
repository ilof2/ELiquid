from user_related_models.controller import get_user_info
from users.controller import register


def test_init_user_info_on_user_create(user_dict):
    user = register(**user_dict)
    user_info = get_user_info(user_id=user.uid)
    assert user_info
    assert user_info.user_id == user.uid
    assert user_info.consumables.flavor == []
    assert user_info.consumables.nicotine == []
    assert user_info.consumables.vg.amount == 0
    assert user_info.consumables.pg.amount == 0
