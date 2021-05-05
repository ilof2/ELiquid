from consumables.pg.models import PG


def test_pg_models(pg_dict):
    pg = PG.create(**pg_dict)
    assert pg.consumable_type == pg_dict['consumable_type']
    assert pg.amount == pg_dict['amount']
    assert pg.uid == pg_dict['_id']

