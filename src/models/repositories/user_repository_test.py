from .user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler


def test_registry_user():
    db_connection_handler.connect()
    connection = db_connection_handler.get_connection()
    repository = UserRepository(connection)

    username = "Barney"
    password = "123Rocket"

    repository.registry_user(username, password)
