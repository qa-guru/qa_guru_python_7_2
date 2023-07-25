import pytest


@pytest.fixture(scope="session")
def user_test():
    print("Тестовый пользователь перед тестом")

    yield

    print("Здесь откатываем тестового пользователя")
