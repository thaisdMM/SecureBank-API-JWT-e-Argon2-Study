from src.models.interfaces.user_repository import UserRepositoryInterface
from src.drivers.jwt_handler import JwtHandler
from src.drivers.password_handler import PasswordHandler


class LoginCreator:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self._user_repository = user_repository
        self._jwt_handler = JwtHandler()
        self._password_handler = PasswordHandler()

    def create(self, username: str, password: str) -> dict:
        # tem que verificar se o usuario existe
        user = self._find_user(username)
        user_id = user[0]
        hashed_password = user[2]

        # verificar se a senha bate com a do banco de dados
        self._verify_correct_password(password, hashed_password)

        token = self._create_jwt_token(user_id)

        return self._format_response(username, token)

    # int: id, str: username, str: password
    def _find_user(self, username: str) -> tuple[int, str, str]:
        user = self._user_repository.get_user_by_username(username)
        if not user:
            raise Exception("User not found")

        return user

    def _verify_correct_password(self, password: str, hashed_password: str) -> None:
        is_password_correct = self._password_handler.verify_password(
            password, hashed_password
        )
        if not is_password_correct:
            raise Exception("Wrong password")

    def _create_jwt_token(self, user_id: int) -> str:
        payload = {"user_id": user_id}
        token = self._jwt_handler.create_jwt_token(payload)
        return token

    def _format_response(self, username: str, token: str) -> dict:
        return {
            "access": True,
            "username": username,
            "token": token,
        }
