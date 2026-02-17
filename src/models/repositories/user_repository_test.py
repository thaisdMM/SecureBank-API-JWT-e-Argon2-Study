from .user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler

# separei o teste do professor em 3 testes:


def test_registry_user():
    db_connection_handler.connect()
    connection = db_connection_handler.get_connection()
    repository = UserRepository(connection)

    username = "Patrick"
    password = "124Rocket"

    # criando registro
    repository.registry_user(username, password)


def test_get_user_by_username():
    db_connection_handler.connect()
    connection = db_connection_handler.get_connection()
    repository = UserRepository(connection)

    # pegando as informações do user
    user = repository.get_user_by_username("Patrick")
    print()
    print(user)


def test_edit_balance():
    db_connection_handler.connect()
    connection = db_connection_handler.get_connection()
    repository = UserRepository(connection)

    # pegando as informações do user
    user = repository.get_user_by_username("Patrick")
    print()
    print(user)

    # editando o balance -
    #  só aparece no print se editar get_user_by_username para mostrar esse dado:
    #  SELECT id, username, password, balance
    repository.edit_balance(user[0], 6672.10)
    user2 = repository.get_user_by_username("Patrick")
    print()
    print(user2)


# esse foi o teste que o professor fez, ele fez tudo junto,
# depois mudou só para get_user_by_username  para não ficar sempre inserindo dados no banco


def test_repository():
    db_connection_handler.connect()
    connection = db_connection_handler.get_connection()
    repository = UserRepository(connection)

    username = "Bob Esponja"
    password = "123Rocket"

    # criando registro
    repository.registry_user(username, password)

    # pegando as informações do user
    user = repository.get_user_by_username(username)
    print()
    print(user)

    repository.edit_balance(user[0], 6672.10)
    user2 = repository.get_user_by_username(username)
    print()
    print(user2)
