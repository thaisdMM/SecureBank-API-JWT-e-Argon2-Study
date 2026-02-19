from src.models.interfaces.user_repository import UserRepositoryInterface
from src.drivers.jwt_handler import JwtHandler
from src.drivers.password_handler import PasswordHandler
from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.types.http_bad_request import HttpBadRequestError
from .interfaces.login_creator import LoginCreatorInterface


class LoginCreator(LoginCreatorInterface):
    """
    Caso de Uso: Realiza a autenticação do usuário e gera o token de acesso.
    """

    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self._user_repository = user_repository
        self._jwt_handler = JwtHandler()
        self._password_handler = PasswordHandler()

    def create(self, username: str, password: str) -> dict:
        """
        Orquestra o fluxo de login: busca usuário, valida senha e gera token.

        Args:
            username (str): Nome de usuário fornecido.
            password (str): Senha em texto puro.

        Returns:
            dict: Resposta formatada com o status de acesso e o token JWT.
        """
        # 1. Busca os dados do usuário no banco de dados
        user = self._find_user(username)
        user_id = user[0]
        hashed_password = user[2]

        # 2. Compara o hash do banco com a senha digitada usando Argon2
        self._verify_correct_password(password, hashed_password)

        # 3. Cria o token de acesso contendo o ID do usuário
        token = self._create_jwt_token(user_id)

        return self._format_response(username, token)

    # int: id, str: username, str: password
    def _find_user(self, username: str) -> tuple[int, str, str]:
        """Busca usuário no repositório e valida existência."""
        user = self._user_repository.get_user_by_username(username)
        if not user:
            raise HttpNotFoundError("Usuário não encontrado")
        return user

    def _verify_correct_password(self, password: str, hashed_password: str) -> None:
        """Utiliza o driver de password para validar a integridade da senha."""
        is_password_correct = self._password_handler.verify_password(
            password, hashed_password
        )
        if not is_password_correct:
            raise HttpBadRequestError("Senha incorreta")

    def _create_jwt_token(self, user_id: int) -> str:
        """Encapsula a criação do payload para o handler de JWT."""
        payload = {"user_id": user_id}
        token = self._jwt_handler.create_jwt_token(payload)
        return token

    def _format_response(self, username: str, token: str) -> dict:
        """Padroniza o retorno para a camada de visualização (View)."""
        return {
            "access": True,
            "username": username,
            "token": token,
        }
