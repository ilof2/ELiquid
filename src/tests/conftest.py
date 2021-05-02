from pytest import fixture


@fixture()
def user_dict():
    obj = {
        "username": "test",
        "password": "123",
        "email": "test@test.com",
    }
    return obj


@fixture()
def ten_users_generator():
    def users():
        for name_num in range(10):
            obj = {
                "username": f"test{name_num}",
                "password": "123",
                "email": f"test{name_num}@test.comm",
            }
            yield obj
    return users()
