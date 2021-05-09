from bson import ObjectId

from user_related_models.controller import init_user_info, get_user_info
from user_related_models.models import UserInfo


def test_init_and_get_user_info():
    user_id = ObjectId()
    init_user_info(user_id=user_id)
    user_info: UserInfo = get_user_info(user_id=user_id)
    assert user_info.user_id == user_id
    consumables = user_info.consumables
    assert consumables.vg.uid
    assert consumables.vg.amount == 0
    assert consumables.pg.uid
    assert consumables.pg.amount == 0
    assert len(consumables.nicotine) == 0
    assert len(consumables.flavor) == 0


def test_get_not_existing_user_info():
    user_info = get_user_info(user_id=ObjectId())
    assert user_info is None
