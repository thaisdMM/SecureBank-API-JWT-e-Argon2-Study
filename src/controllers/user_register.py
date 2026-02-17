from src.models.interfaces.user_repository import UserRepositoryInterface
from src.drivers.password_handler import PasswordHandler


class UserRegister:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self._user_repository = user_repository
        self._password_handle = PasswordHandler()

    def registry(self, username: str, password: str) -> dict:
        """
        Registra um usuário e senha usando os métodos privados de
        criação de hashed password, registro de novo usuário no banco de dados e resposta formatada
        """
        hashed_password = self._create_hash_password(password)
        self._registry_new_user(username, hashed_password)
        return self._format_response(username)

    # método protegido
    def _create_hash_password(self, passsword: str) -> str:
        """Cria a senha hashed"""
        hashed_password = self._password_handle.hash_password(passsword)
        return hashed_password

    def _registry_new_user(self, username: str, hashed_password: str) -> None:
        """Faz o registro do usuário no banco de dados"""
        self._user_repository.registry_user(username, hashed_password)

    def _format_response(self, username: str) -> dict:
        """Formata uma resposta"""
        return {"type": "User", "count": 1, "username": username}
