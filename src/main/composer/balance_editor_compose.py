from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.balance_editor import BalanceEditor
from src.views.balance_editor_view import BalanceEditorView


def balance_editor_composer():
    connection = db_connection_handler.get_connection()
    model = UserRepository(connection)
    controller = BalanceEditor(model)
    view = BalanceEditorView(controller)
    
    return view
