import pytest

from src.drivers.password_handler import PasswordHandler
from .login_creator import LoginCreator


username = "MeuUsername"
password = "MinhaSenha"
# deveria ser a senha do banco de dados
hashed_password = PasswordHandler().hash_password(password)


class MockUserRepository:
    def get_user_by_username(self, username: str):
        """Mock para retornar dados simulando banco de dados"""
        return (10, username, hashed_password)


def test_create():

    login_creator = LoginCreator(MockUserRepository())
    response = login_creator.create(username, password)

    assert response["access"] == True
    assert response["username"] == username
    assert response["token"] is not None


def test_create_wrong_password():

    login_creator = LoginCreator(MockUserRepository())

    with pytest.raises(Exception, match="Senha incorreta"):
        login_creator.create(username, "senhaErrada")
