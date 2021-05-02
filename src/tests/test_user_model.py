from src.users.models import User


def test_user_create():
    user = User.create("test", "test@test.com", "123")
    assert user
    assert user.username == "test"
    assert User.check_password(user.password, "123")
