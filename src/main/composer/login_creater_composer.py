from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.login_creator import LoginCreator
from src.views.login_creator_view import LoginCreatorView


def login_creator_composer():
    connection = db_connection_handler.get_connection()
    models = UserRepository(connection)
    controller = LoginCreator(models)
    view = LoginCreatorView(controller)

    return view
