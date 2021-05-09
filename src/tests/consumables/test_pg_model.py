from user_info.consumables import PG


def test_pg_models(pg_dict_db):
    pg = PG.create_from_db(**pg_dict_db)
    assert pg.uid == pg_dict_db['_id']
    assert pg.amount == pg_dict_db['amount']

