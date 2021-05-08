from user_related_models.consumables import PG


def test_pg_models(pg_dict_db):
    pg = PG.create_from_db(**pg_dict_db)
    assert pg.uid == pg_dict_db['uid']
    assert pg.amount == pg_dict_db['amount']

