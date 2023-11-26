import pytest

from models.user import User

@pytest.fixture(scope="module")


def test_create_user():
    # SETUP
    user_name = "test_user"
    password = "ThisIsComplicatedPassword"

    # RUN
    new_user = User(user_name=user_name, password=password)

    sql_template, user_creation_values = new_user.__create_model_sql__()
    # ASSERT
    assert type(new_user) == User
    assert type(new_user.user_id) == str
    assert type(new_user.created_on) == str
    assert new_user.user_name == user_name
    assert new_user.password == password
    assert user_creation_values[0] == new_user.user_id
    assert user_creation_values[1] == user_name
    assert user_creation_values[2] == password
    assert user_creation_values[0] == new_user.created_on
    